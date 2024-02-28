from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from models.reply import Reply
from services.reply_service import ReplyService

class ReplyListView(MethodView):

    def __init__(self):
        self.reply_service = ReplyService()

    def post(self, post_id):
        reply_data = request.get_json()
        print(reply_data)
        success, message = self.reply_service.create_reply(reply_data)
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400

    def get(self, post_id):
        reply_list = self.reply_service.get_all_replies_by_post(post_id)
        return jsonify([reply.serialize() for reply in reply_list])

class ReplyDetailView(MethodView):
    def __init__(self):
        self.reply_service = ReplyService()

    def get(self, post_id, reply_id):
        reply = jsonify(self.reply_service.get_reply_by_id(post_id,reply_id).serialize())
        return jsonify(self.reply_service.get_reply_by_id(post_id,reply_id).serialize())