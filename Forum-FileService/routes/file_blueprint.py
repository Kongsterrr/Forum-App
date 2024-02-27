from flask import Blueprint
from controllers.file_controller import FileView

file_blueprint = Blueprint('file', __name__, url_prefix='/file')
file_blueprint.add_url_rule('/upload', view_func=FileView.as_view('file-upload'), methods=['POST'])
file_blueprint.add_url_rule('/get/<filename>', view_func=FileView.as_view('file-get'), methods=['GET'])
file_blueprint.add_url_rule('/delete/<filename>', view_func=FileView.as_view('file-delete'), methods=['DELETE'])