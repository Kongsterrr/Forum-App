from flask import jsonify, request
from flask.views import MethodView
from services.postDetail_service import PostDetailService
from aop.decorators import token_required



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


class AdminHomeView(MethodView):

    def __init__(self):
        self.admin_home_service = PostDetailService()

    @token_required
    def get(self, user_id, user_status):
        success, user_home = self.admin_home_service.get_admin_home(user_status)
        if not success:
            return jsonify({'error': user_home}), 403
        return jsonify(user_home), 200