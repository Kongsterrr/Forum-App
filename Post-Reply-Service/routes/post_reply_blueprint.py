from flask import Blueprint

from controllers.post_controller import *
from controllers.reply_controller import *

post_reply_blueprint = Blueprint('post_and_reply', __name__, url_prefix='/post_and_reply')
post_reply_blueprint.add_url_rule('/', view_func=PostCreateView.as_view('create_post'), methods=['POST'])
post_reply_blueprint.add_url_rule('/<int:post_id>', view_func=PostDetailView.as_view('detail_and_update'), methods=['GET', 'PUT'])
post_reply_blueprint.add_url_rule('/<int:post_id>/hide', view_func=HidePostView.as_view('hide_post'), methods=['PUT'])
post_reply_blueprint.add_url_rule('/<int:post_id>/delete', view_func=DeletePostView.as_view('delete_post'), methods=['PUT'])
post_reply_blueprint.add_url_rule('/<int:post_id>/archive', view_func=ArchivePostView.as_view('archive_post'), methods=['PUT'])
post_reply_blueprint.add_url_rule('/<int:post_id>/publish', view_func=PublishPostView.as_view('publish_post'), methods=['PUT'])
post_reply_blueprint.add_url_rule('/<int:post_id>/recoverDeleted', view_func=RecoverDeleteToPublishedPostView.as_view('recover_deleted_post'), methods=['PUT'])
post_reply_blueprint.add_url_rule('/<int:post_id>/banned', view_func=BannedPostView.as_view('ban_post'), methods=['PUT'])
post_reply_blueprint.add_url_rule('/<int:post_id>/unbanned', view_func=UnBannedPostView.as_view('unban_post'), methods=['PUT'])
post_reply_blueprint.add_url_rule('/published-post', view_func=AllPublishedPostView.as_view('view-all-published'), methods=['GET'])
post_reply_blueprint.add_url_rule('/top', view_func=Top3PostsView.as_view('Top-3-posts'), methods=['GET'])
post_reply_blueprint.add_url_rule('/drafts', view_func=AllUnpublishedPostsView.as_view('drafts'), methods=['GET'])
post_reply_blueprint.add_url_rule('/all-banned-posts', view_func=AllBannedPostView.as_view('all_ban_post'), methods=['GET'])
post_reply_blueprint.add_url_rule('/all-deleted-posts', view_func=AdminGetDeletePostView.as_view('all_deleted_post'), methods=['GET'])
post_reply_blueprint.add_url_rule('/all-hidden-posts', view_func=AllHiddenPostView.as_view('all_hidden_post'), methods=['GET'])


post_reply_blueprint.add_url_rule('/<int:post_id>/reply', view_func=ReplyListView.as_view('reply_list_and_create'), methods=['POST', 'GET'])
post_reply_blueprint.add_url_rule('/<int:post_id>/reply/<int:reply_id>', view_func=ReplyDetailView.as_view('reply_detail'), methods=['GET'])
