from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from models.reply import Reply
from services.reply_service import ReplyService

class ReplyCreateView(MethodView):

    def __init__(self):
        self.reply_service = ReplyService()

    def post(self):
        reply_data = request.get_json()
        success, message = self.reply_service.create_reply(reply_data)
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400

class ReplyDetailView(MethodView):
    def __init__(self):
        self.reply_service = ReplyService()

    def get(self, reply_id):
        return jsonify(self.reply_service.get_reply_by_id(reply_id).serialize())