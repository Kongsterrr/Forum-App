from flask import Blueprint
from controllers.message_controller import MessageView

message_blueprint = Blueprint('messages', __name__, url_prefix='/messages')

message_blueprint.add_url_rule('/', view_func=MessageView.as_view('messages'), methods=['POST', 'GET'])
message_blueprint.add_url_rule('/<int:messageId>', view_func=MessageView.as_view('messages_patch'), methods=['PATCH'])
