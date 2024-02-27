from flask import jsonify, request
from flask.views import MethodView

from services.auth_service import AuthService

class UserRegisterView(MethodView):

    def __init__(self):
        self.auth_service = AuthService()  
    
    def post(self):  
        data = request.get_json()
        print(data)
        if 'user_id' not in data:
            return jsonify({'error': 'User id not provided'}), 400

        user_id = data['user_id']
        return jsonify(self.auth_service.set_user_token(user_id))

class SendEmailView(MethodView):

    def __init__(self):
        self.auth_service = AuthService()  

    def post(self):  
        data = request.get_json()

        if 'user_id' not in data:
            return jsonify({'error': 'User id not provided'}), 400
        
        if 'user_email' not in data:
            return jsonify({'error': 'User email not provided'}), 400
        
        if 'token' not in data:
            return jsonify({'error': 'User token not provided'}), 400

        user_email = data['user_email']
        user_id = data['user_id']
        token = data['token']
        return jsonify(self.auth_service.send_email_to_queue(user_email, user_id, token))

class TokenVerifyView(MethodView):

    def __init__(self):
        self.auth_service = AuthService()  
    
    def post(self):  
        data = request.get_json()

        if 'user_id' not in data:
            return jsonify({'error': 'User id not provided'}), 400

        if 'token' not in data:
            return jsonify({'error': 'User token not provided'}), 400
        
        user_id = data['user_id']
        token = data['token']

        return jsonify(self.auth_service.verify_user_token(user_id, token))

class CodeVerifyView(MethodView):

    def __init__(self):
        self.auth_service = AuthService()  
        
    def post(self):  
        data = request.get_json()

        if 'user_id' not in data:
            return jsonify({'error': 'User id not provided'}), 400

        if 'verification_code' not in data:
            return jsonify({'error': 'User verification code not provided'}), 400
        
        if 'token' not in data:
            return jsonify({'error': 'User token not provided'}), 400
        
        user_id = data['user_id']
        verification_code = data['verification_code']
        token = data['token']

        return jsonify(self.auth_service.verify_user_code(user_id, verification_code, token))

