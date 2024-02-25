from flask import jsonify, request
from flask.views import MethodView

from models.post import Post
from services.post_service import PostService


class PostView(MethodView):
    def __init__(self):
        self.post_service = PostService()

    def get(self, post_id):
        return jsonify(self.post_service.get_post(post_id).serialize())

