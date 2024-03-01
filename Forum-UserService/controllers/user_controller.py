from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from models.user import User
from services.user_service import UserService


class UserView(MethodView):

    def __init__(self):
        self.user_service = UserService()

    def get(self, user_id):
        return jsonify(self.user_service.get_user(user_id).serialize())

    @token_required
    def put(self, current_user, user_id):  # current_user is injected by the decorator, must be the first argument
        return jsonify(request.json), 200


class UserRegisterView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def post(self):
        user_data = request.get_json()
        success, message, user_id = self.user_service.create_user(user_data)
        if success:
            return jsonify({'message': message, 'user_id': user_id}), 201
        else:
            return jsonify({'message': message, 'user_id': user_id}), 400


class UserLoginView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def post(self):
        data = request.get_json()
        user_id, user_status = self.user_service.authenticate_user(data['email'], data['password'])

        if user_id:
            return jsonify({'Authentication status': 'Success', 'user_id': user_id, 'user_status': user_status}), 200

        return jsonify({'Authentication status': 'Failure'}), 401


class UserProfileView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    # @token_required
    def get(self, user_id):
        user_profile = self.user_service.get_user_profile(user_id)
        if user_profile:
            return jsonify(user_profile), 200
        else:
            return jsonify({"message": "User not found"}), 404

class UserEmailVerificationView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def get(self, user_id):
        return jsonify(self.user_service.send_verification_code(user_id))
    
    def post(self, user_id):

        data = request.get_json()

        if 'verification_code' not in data:
            return jsonify({'error': 'Verification code not provided'}), 400

        verification_code = data['verification_code']

        return jsonify(self.user_service.verify_user(user_id, verification_code))

class UserProfileUpdateView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def post(self, user_id):

        data = request.get_json()

        if 'update_type' not in data:
                return jsonify({'error': 'Update type not provided'}), 400

        update_type = data.get('update_type')

        if update_type == 'picture':
            if 'url' not in data:
                return jsonify({'error': 'Profile picture url not provided'}), 400
            url = data['url']
            return jsonify(self.user_service.update_profile_pic(user_id, url))

        if update_type == 'email':
            if 'email' not in data:
                return jsonify({'error': 'User email not provided'}), 400
            email = data['email']
            return jsonify(self.user_service.update_user_email(user_id, email))
        
        return jsonify({'error': 'Update type invalid.'}), 400




