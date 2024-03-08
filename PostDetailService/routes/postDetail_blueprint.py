from flask import Blueprint

from controllers.postDetail_controller import *

postDetail_blueprint = Blueprint('post-details', __name__, url_prefix='/post-details')

postDetail_blueprint.add_url_rule('/<int:post_id>', view_func=PostDetailView.as_view('post_details'), methods=['GET'])
postDetail_blueprint.add_url_rule('/', view_func=UserHomeView.as_view('user_home'), methods=['GET'])
postDetail_blueprint.add_url_rule('/admin', view_func=AdminHomeView.as_view('admin_home'), methods=['GET'])
postDetail_blueprint.add_url_rule('/top', view_func=TopPostView.as_view('top_post'), methods=['GET'])