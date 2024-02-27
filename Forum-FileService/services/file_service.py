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

    def upload_file(self, file_path):
        try:
            filename = secure_filename(file_path.split("/")[-1]) 
            extra_args = {
                'ContentType': 'image/png' 
            }
            self.s3_client.upload_file(file_path, self.bucket_name, filename, ExtraArgs=extra_args)
            self.s3_client.upload_file(file_path, self.bucket_name, filename)
            return {'message': 'File uploaded successfully'}
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
                                                        ExpiresIn=3600,
                                                        HttpMethod='GET',
                                                        )
            return url
        except Exception as e:
            return {'error': str(e)}
