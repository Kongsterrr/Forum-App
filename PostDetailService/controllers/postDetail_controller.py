from flask import jsonify, request
from flask.views import MethodView
from services.postDetail_service import PostDetailService


class PostDetailView(MethodView):

    def __init__(self):
        self.post_detail_service = PostDetailService()

    def get(self, post_id):
        post_detail = self.post_detail_service.get_post_detail(post_id)
        return jsonify(post_detail), 200