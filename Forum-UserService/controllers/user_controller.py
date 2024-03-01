from flask import jsonify, request
from flask.views import MethodView

from aop.decorators import token_required
from models.user import User
from services.user_service import UserService


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
        print("haha")
        return jsonify(self.user_service.send_verification_code(user_id))
    
    def post(self, user_id):

        data = request.get_json()

        if 'verification_code' not in data:
            return jsonify({'error': 'Verification code not provided'}), 400

        verification_code = data['verification_code']

        return jsonify(self.user_service.verify_user(user_id, verification_code))


class UserStatusUpgradeView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    @token_required
    def put(self, userId, user_id, user_status):
        success, message = self.user_service.upgrade_to_admin(userId, user_status)
        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'error': message}), 404
