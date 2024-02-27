from flask import jsonify, request
from flask.views import MethodView

from services.file_service import FileService


class FileView(MethodView):

    def __init__(self):
        self.file_service = FileService()  

    def post(self):  
        data = request.get_json()
        if 'file_path' not in data:
            return jsonify({'error': 'File path not provided'}), 400

        file_path = data['file_path']

        return jsonify(self.file_service.upload_file(file_path))
    
    def get(self, filename):
        return jsonify(self.file_service.get_file(filename))


    def delete(self, filename):
        return jsonify(self.file_service.delete_file(filename))

