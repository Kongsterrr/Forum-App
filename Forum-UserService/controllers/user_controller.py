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
        success, message = self.user_service.create_user(user_data)
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400


class UserLoginView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def post(self):
        data = request.get_json()
        token = self.user_service.get_user_token(data['email'], data['password'])
        return jsonify({'token': token}), 200


class UserProfileView(MethodView):
    def __init__(self):
        self.user_service = UserService()

    @token_required
    def get(self, current_user, user_id):
        user_profile = self.user_service.get_user_profile(user_id)
        if user_profile:
            return jsonify(user_profile), 200
        else:
            return jsonify({"message": "User not found"}), 404




