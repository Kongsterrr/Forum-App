from flask import request, jsonify

from aop.exceptions import AuthorizationError, RequestDataError, InvalidTokenError
from services.message_service import MessageService
from flask.views import MethodView
import jwt
import config
from aop.decorators import token_required

class MessageView(MethodView):
    def __init__(self):
        self.message_service = MessageService()

    @token_required
    def post(self, user_id, user_status):
        if user_status == 'Admin':
            raise AuthorizationError("Admins are not allowed to create messages")

        # Check if the request has a JSON content type
        if request.content_type == 'application/json':
            message_data = request.json
            if not message_data:
                raise RequestDataError("Request data is missing")  # request body: {}
        else:
            # The content type is not JSON
            raise RequestDataError(f"Unsupported content type: {request.content_type}")  # includes empty request body

        result = self.message_service.create_message(user_id, message_data)
        return jsonify(result)

    @token_required
    def get(self, user_id, user_status):
        if user_status != 'Admin':
            raise AuthorizationError("Only admins are allowed to get all messages")

        messages = self.message_service.get_all_messages()
        return jsonify(messages)

    @token_required
    def patch(self, user_id, user_status, messageId):
        if user_status != 'Admin':
            raise AuthorizationError("Only admins are allowed to update message status")

        status = request.args.get('status')
        if not status or status not in ['Open', 'Close']:
            raise RequestDataError("Invalid status provided")

        result = self.message_service.update_message_status(messageId, status)
        return jsonify(result)