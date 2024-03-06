from datetime import datetime

from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from services.post_history_service import PostHistoryService


class PostHistoryController(MethodView):
    def __init__(self):
        self.post_history_service = PostHistoryService()

    @token_required
    def get(self, user_id, user_status):
        post_history_result = self.post_history_service.get_post_history(user_id)
        return jsonify({"post_history": post_history_result})


        history_result = self.history_service.get_history_by_user(user_id)
        if not history_result:
            return jsonify(history_result)
        print(history_result[0].serialize())

        return jsonify([res.serialize() for res in history_result])

