from datetime import datetime

from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from models.history import History
from services.history_service import HistoryService


class HistoryController(MethodView):
    def __init__(self):
        self.history_service = HistoryService()

    def get(self, uid):
        history_result = self.history_service.get_history_by_user(uid)
        if not history_result:
            return jsonify({"histories": []})
        return jsonify({"histories": [res.serialize() for res in history_result]})

class HistoryCreateController(MethodView):
    def __init__(self):
        self.history_service = HistoryService()
    @token_required
    def post(self, user_id, user_status):
        try:
            post_id = request.json['postId']
        except KeyError:
            return jsonify({'message': 'postId is missing in request'}), 400

        history_data = {
            'userId': user_id,
            'postId': post_id,
            'viewDate': datetime.utcnow()
        }

        success, message = self.history_service.create_history(history_data)

        if success:
            return jsonify({'message': message, 'uid': history_data['userId']}), 201
        else:
            return jsonify({'message': message}), 400