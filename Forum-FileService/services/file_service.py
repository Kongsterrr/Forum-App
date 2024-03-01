import boto3
from werkzeug.utils import secure_filename
import json

class FileService:
    def __init__(self):

        with open('config.json') as f:
            config = json.load(f)
        
        self.bucket_name = config["AWS_BUCKET_NAME"]
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=config["AWS_ACCESS_KEY"],
            aws_secret_access_key=config["AWS_SECRET_KEY"],
            region_name=config["AWS_BUCKET_REGION"]
        )

    def upload_file(self, user_id, file_path):
        try:
            filename = str(user_id) + "-" + secure_filename(file_path.split("/")[-1]) 
            self.s3_client.upload_file(file_path, self.bucket_name, filename)
            url = self.get_file(filename)
            return {'message': 'File uploaded successfully', 'url': url}
        except Exception as e:
            return {'error': str(e)}
    
    def upload_files(self, user_id, file_paths):
        try:
            urls = []
            for file_path in file_paths:
                filename = str(user_id) + "-post-" + secure_filename(file_path.split("/")[-1]) 
                self.s3_client.upload_file(file_path, self.bucket_name, filename)
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
                                                        )
            return url
        except Exception as e:
            return {'error': str(e)}
