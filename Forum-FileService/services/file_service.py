import os
import uuid
import boto3
from werkzeug.utils import secure_filename
import json
import config
import base64
from PIL import Image
from io import BytesIO

class FileService:
    def __init__(self):

        self.bucket_name = config.AWS_BUCKET_NAME
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=config.AWS_ACCESS_KEY,
            aws_secret_access_key=config.AWS_SECRET_KEY,
            region_name=config.AWS_BUCKET_REGION
        )

    def decode_file(self, user_id, file_path, data_string):

        image_data = base64.b64decode(data_string)
        image = Image.open(BytesIO(image_data))

        # Generate a unique filename
        filename = str(user_id) + "-" + secure_filename(file_path.split("/")[-1]) + '.png'

        temp_filepath = os.path.join('/tmp', filename)
        image.save(temp_filepath)
        return filename, temp_filepath

    def upload_file(self, user_id, file_path, file_object):
        print("Uploading file: ", user_id, file_path)
        try:
            # Save file to tmp, generate file name and path
            filename, filepath = self.decode_file(user_id, file_path, file_object)
   
            # Upload the file to S3
            self.s3_client.upload_file(filepath, self.bucket_name, filename)

            # self.s3_client.upload_fileobj(file_object, self.bucket_name, filename)
            url = self.get_file(filename)
            return {'message': 'File uploaded successfully', 'url': url}
        except Exception as e:
            print(e)
            return {'error': str(e)}
    
    '''
    files: list: [file_info]
    file_info: tuple: (file_path, file_object)
    '''
    def upload_files(self, user_id, files):
        try:
            urls = []
            for file_info in files:
                file_path = file_info[0]
                file_object = file_info[1]
                filename, filepath = self.decode_file(user_id, file_path, file_object)
                self.s3_client.upload_file(filepath, self.bucket_name, filename)
                url = self.get_file(filename)
                urls.append(url)
            return {'message': 'Files uploaded successfully', 'urls': urls}
        except Exception as e:
            return {'error': str(e)}

    def delete_file(self, filename):
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=filename)
            return {'message': f'File {filename} deleted successfully'}
        except Exception as e:
            return {'error': str(e)}
    
    def get_file(self, file_name):
        try:
            url = self.s3_client.generate_presigned_url('get_object', 
                                                        Params={'Bucket': self.bucket_name, 'Key': file_name},
                                                        HttpMethod='GET',
                                                        ExpiresIn=31536000,
                                                        )
            return url
        except Exception as e:
            return {'error': str(e)}
