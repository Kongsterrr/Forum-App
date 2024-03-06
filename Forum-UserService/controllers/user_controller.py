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

    @token_required
    def get(self, user_id, user_status):
        user_profile = self.user_service.get_user_profile(user_id)
        if user_profile:
            return jsonify(user_profile.serialize()), 200
        else:
            return jsonify({"message": "User not found"}), 404

class UserEmailVerificationView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    @token_required
    def get(self, user_id, user_status):
        return jsonify(self.user_service.send_verification_code(user_id))
    
    @token_required
    def post(self, user_id, user_status):

        data = request.get_json()

        print(data)

        if 'verification_code' not in data:
            return jsonify({'error': 'Verification code not provided'}), 400

        verification_code = data['verification_code']

        return jsonify(self.user_service.verify_user(user_id, verification_code))

class UserProfileUpdateView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    @token_required
    def post(self, user_id, user_status):

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


class AdminAllUserProfileView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    @token_required
    def get(self, user_id, user_status):
        success, result = self.user_service.get_all_user(user_status)
        if not success:
            return jsonify({'error': result}), 403
        return jsonify([user.serialize() for user in result]), 200


class BanUserView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    @token_required
    def put(self, userId, user_id, user_status):
        success, result = self.user_service.ban_user(userId, user_status)
        if success:
            return jsonify({'results': result}), 200
        else:
            return jsonify({'error': result}), 404


class UnBanUserView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    @token_required
    def put(self, userId, user_id, user_status):
        success, result = self.user_service.unban_user(userId, user_status)
        if success:
            return jsonify({'results': result}), 200
        else:
            return jsonify({'error': result}), 404

