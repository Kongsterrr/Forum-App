from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from models.post import Post
from services.post_service import PostService


class PostDetailView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    # @token_required
    def get(self, post_id):
        return jsonify(self.post_service.get_post(post_id).serialize())

    # @token_required
    def put(self, post_id):
        post_data = request.get_json()
        success, message = self.post_service.update_post(post_id, post_data)
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'message': message}), 400


class PostCreateView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    # @token_required
    def post(self):
        post_data = request.get_json()
        success, message = self.post_service.create_post_published(post_data)
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400



class PublishPostView(MethodView):
    # @token_required
    # def put(self, post_id, current_user):
    # success, message = PostService().publish_post(post_id, current_user.user_id)
    # return jsonify({'message': message}), 200 if success else 400
    def put(self, post_id):
        success, message = PostService().publish_post(post_id)

        return jsonify({'message': message}), 200 if success else 400


class HidePostView(MethodView):
    # @token_required
    # def put(self, post_id, current_user):
    # success, message = PostService().hide_post(post_id, current_user.user_id)
    # return jsonify({'message': message}), 200 if success else 400
    def put(self, post_id):
        success, message = PostService().hide_post(post_id)

        return jsonify({'message': message}), 200 if success else 400


class DeletePostView(MethodView):
    # @token_required
    # def put(self, post_id, current_user):
    # success, message = PostService().delete_post(post_id, current_user.user_id)
    # return jsonify({'message': message}), 200 if success else 400
    def put(self, post_id):
        success, message = PostService().delete_post(post_id)
        return jsonify({'message': message}), 200 if success else 400


class ArchivePostView(MethodView):
    # @token_required
    # def put(self, post_id, current_user):
    # success, message = PostService().archive_post(post_id, current_user.user_id)
    # return jsonify({'message': message}), 200 if success else 400
    def put(self, post_id):
        success, message = PostService().archive_post(post_id)

        return jsonify({'message': message}), 200 if success else 400


# For Admin
class RecoverDeleteToPublishedPostView(MethodView):
    def put(self, post_id):
        success, message = PostService().recover_post(post_id)

        return jsonify({'message': message}), 200 if success else 400


# For Admin
class BannedPostView(MethodView):
    def put(self, post_id):
        success, message = PostService().ban_post(post_id)

        return jsonify({'message': message}), 200 if success else 400


# For Admin
class UnBannedPostView(MethodView):
    def put(self, post_id):
        success, message = PostService().unbanned_post(post_id)

        return jsonify({'message': message}), 200 if success else 400
