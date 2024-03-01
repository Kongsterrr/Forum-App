from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from models.post import Post
from services.post_service import PostService


class PostDetailView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    def get(self, post_id):
        return jsonify(self.post_service.get_post(post_id).serialize())

    @token_required
    def put(self, post_id, user_id, user_status):
        post_data = request.get_json()
        success, message = self.post_service.update_post(post_id, post_data, user_id)
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'message': message}), 400


class PostCreateView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def post(self, user_id, user_status):
        post_data = request.get_json()
        success, message = self.post_service.create_post_published(post_data, user_id)
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400


class PublishPostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def put(self, post_id, user_id, user_status):
        success, message = self.post_service.publish_post(post_id, user_id)
        return jsonify({'message': message}), 200 if success else 400


class HidePostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def put(self, post_id, user_id, user_status):
        success, message = self.post_service.hide_post(post_id, user_id)
        return jsonify({'message': message}), 200 if success else 400


class DeletePostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def put(self, post_id, user_id, user_status):
        success, message = self.post_service.delete_post(post_id, user_id)
        return jsonify({'message': message}), 200 if success else 400


class ArchivePostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def put(self, post_id, user_id, user_status):
        success, message = self.post_service.archive_post(post_id, user_id)
        return jsonify({'message': message}), 200 if success else 400


# For Admin
class RecoverDeleteToPublishedPostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def put(self, post_id, user_id, user_status):
        success, message = self.post_service.recover_post(post_id, user_status)
        return jsonify({'message': message}), 200 if success else 400


# For Admin
class BannedPostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def put(self, post_id, user_id, user_status):
        success, message = self.post_service.ban_post(post_id, user_status)
        return jsonify({'message': message}), 200 if success else 400


# For Admin
class UnBannedPostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def put(self, post_id, user_id, user_status):
        success, message = self.post_service.unbanned_post(post_id, user_status)
        return jsonify({'message': message}), 200 if success else 400


class AllPublishedPostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    def get(self):
        posts = self.post_service.fetch_published_posts()
        posts_data = [post.serialize() for post in posts]
        return jsonify(posts_data), 200


class Top3PostsView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def get(self, user_id, user_status):
        top_posts = self.post_service.get_top_user_posts(user_id)
        result = [{
            'postId': post.Post.postId,
            'title': post.Post.title,
            'replyCount': post.reply_count
        } for post in top_posts]

        return jsonify(result)


class AllUnpublishedPostsView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def get(self, user_id, user_status):
        drafts = self.post_service.get_unpublished_posts(user_id)
        return jsonify([draft.serialize() for draft in drafts]), 200


class AllBannedPostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def get(self, user_id, user_status):
        success, result = self.post_service.get_ban_post(user_status)
        if not success:
            return jsonify({'error': result}), 403
        return jsonify([ban_post.serialize() for ban_post in result]), 200


class AdminGetDeletePostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def get(self, user_id, user_status):
        success, result = self.post_service.get_delete_post(user_status)
        if not success:
            return jsonify({'error': result}), 403
        return jsonify([delete_post.serialize() for delete_post in result]), 200


class AllHiddenPostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    @token_required
    def get(self, user_id, user_status):
        result = self.post_service.get_hidden_post(user_id)
        return jsonify([hidden_post.serialize() for hidden_post in result]), 200
