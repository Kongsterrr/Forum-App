from flask import Blueprint

from controllers.post_controller import *

post_blueprint = Blueprint('user', __name__, url_prefix='/posts')
post_blueprint.add_url_rule('', view_func=PostCreateView.as_view('create_post'), methods=['POST'])
post_blueprint.add_url_rule('/<int:post_id>', view_func=PostDetailView.as_view('detail_and_update'), methods=['GET', 'PUT'])
post_blueprint.add_url_rule('/<int:post_id>/hide', view_func=HidePostView.as_view('hide_post'), methods=['PUT'])
post_blueprint.add_url_rule('/<int:post_id>/delete', view_func=DeletePostView.as_view('delete_post'), methods=['PUT'])
post_blueprint.add_url_rule('/<int:post_id>/archive', view_func=ArchivePostView.as_view('archive_post'), methods=['PUT'])
post_blueprint.add_url_rule('/<int:post_id>/publish', view_func=PublishPostView.as_view('publish_post'), methods=['PUT'])
post_blueprint.add_url_rule('/<int:post_id>/recoverDeleted', view_func=RecoverDeleteToPublishedPostView.as_view('recover_deleted_post'), methods=['PUT'])
post_blueprint.add_url_rule('/<int:post_id>/banned', view_func=BannedPostView.as_view('ban_post'), methods=['PUT'])
post_blueprint.add_url_rule('/<int:post_id>/unbanned', view_func=UnBannedPostView.as_view('unban_post'), methods=['PUT'])