from flask import jsonify, request
from flask.views import MethodView

from services.file_service import FileService


class FileView(MethodView):

    def __init__(self):
        self.file_service = FileService()  

    def post(self):  
        data = request.get_json()

        if 'user_id' not in data:
            return jsonify({'error': 'User id not provided'}), 400
        
        if 'file_path' not in data:
            return jsonify({'error': 'File path not provided'}), 400

        file_path = data['file_path']
        user_id = data['user_id']
        return jsonify(self.file_service.upload_file(user_id, file_path))
    
    def get(self, filename):
        return jsonify(self.file_service.get_file(filename))

    def delete(self, filename):
        return jsonify(self.file_service.delete_file(filename))

class MultiFileView(MethodView):

    def __init__(self):
        self.file_service = FileService()  

    def post(self):  
        data = request.get_json()

        if 'user_id' not in data:
            return jsonify({'error': 'User id not provided'}), 400
        
        if 'file_paths' not in data:
            return jsonify({'error': 'File paths not provided'}), 400

        file_paths = data['file_paths']
        user_id = data['user_id']
        return jsonify(self.file_service.upload_files(user_id, file_paths))
    