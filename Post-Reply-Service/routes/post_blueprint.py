from flask import Blueprint

from controllers.post_controller import *

post_blueprint = Blueprint('user', __name__, url_prefix='/posts')
post_blueprint.add_url_rule('/<int:post_id>', view_func=PostView.as_view('post'), methods=['GET', 'PUT'])
