from flask import jsonify, request
from flask.views import MethodView
from services.postDetail_service import PostDetailService


class PostDetailView(MethodView):

    def __init__(self):
        self.post_detail_service = PostDetailService()

    def get(self, post_id):
        post_detail = self.post_detail_service.get_post_detail(post_id)
        return jsonify(post_detail), 200


class UserHomeView(MethodView):

    def __init__(self):
        self.user_home_service = PostDetailService()

    def get(self):
        user_home = self.user_home_service.get_user_home()
        return jsonify(user_home), 200