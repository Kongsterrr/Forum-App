from flask import Blueprint
from controllers.file_controller import FileView

file_blueprint = Blueprint('file', __name__)
file_blueprint.add_url_rule('/file/upload', view_func=FileView.as_view('file-upload'), methods=['POST'])
file_blueprint.add_url_rule('/file/get/<filename>', view_func=FileView.as_view('file-get'), methods=['GET'])
file_blueprint.add_url_rule('/file/delete/<filename>', view_func=FileView.as_view('file-delete'), methods=['DELETE'])