from flask import jsonify, request
from flask.views import MethodView

from services.auth_service import AuthService


class AuthView(MethodView):

    def __init__(self):
        self.auth_service = AuthService()  

    def post(self):  
        data = request.get_json()
        if 'user_email' not in data:
            return jsonify({'error': 'User email not provided'}), 400

        user_email = data['user_email']

        return jsonify(self.auth_service.send_email_to_queue(user_email))


