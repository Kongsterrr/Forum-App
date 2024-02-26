from flask import Blueprint

from controllers.reply_controller import *

reply_blueprint = Blueprint('reply', __name__, url_prefix='/reply')
reply_blueprint.add_url_rule('', view_func=ReplyCreateView.as_view('create_reply'), methods=['POST'])
# reply_blueprint.add_url_rule('/<int:reply_id>', method=['GET', 'PUT', 'DELETE'])
# reply_blueprint.add_url_rule('/<int:post_id>', method=['GET'])
