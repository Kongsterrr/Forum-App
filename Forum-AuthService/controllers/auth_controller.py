from flask import jsonify, request
from flask.views import MethodView

from services.auth_service import AuthService

class UserRegisterView(MethodView):
    def __init__(self):
        self.auth_service = AuthService() 

    def post(self):
        user_data = request.get_json()
        success, message, user_id = self.auth_service.create_user(user_data)
        if success:
            return jsonify({'message': message, 'user_id': user_id}), 201
        else:
            return jsonify({'message': message, 'user_id': user_id}), 400

class UserLoginView(MethodView):
    def __init__(self):
        self.auth_service = AuthService() 
    
    def post(self):
        data = request.get_json()

        if 'email' not in data:
            return jsonify({'error': 'User email not provided'}), 400
    
        if 'password' not in data:
            return jsonify({'error': 'User password not provided'}), 400
        
        user_email = data['email']
        password = data['password']
        return jsonify(self.auth_service.login_user(user_email, password))


class SendEmailView(MethodView):

    def __init__(self):
        self.auth_service = AuthService()  

    def post(self):  
        data = request.get_json()
        
        if 'user_email' not in data:
            return jsonify({'error': 'User email not provided'}), 400
    
        if 'verification_code' not in data:
            return jsonify({'error': 'User verfication code not provided'}), 400
        
        
        user_email = data['user_email']
        verification_code = data['verification_code']
        return jsonify(self.auth_service.send_email_to_queue(user_email, verification_code))



