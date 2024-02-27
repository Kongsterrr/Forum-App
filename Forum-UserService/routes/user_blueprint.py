from flask import Blueprint

from controllers.user_controller import UserView, UserRegisterView, UserLoginView, UserProfileView

user_blueprint = Blueprint('user', __name__, url_prefix='/user')
user_blueprint.add_url_rule('/<int:user_id>', view_func=UserView.as_view('user'), methods=['GET', 'PUT'])
user_blueprint.add_url_rule('/register', view_func=UserRegisterView.as_view('register_view'), methods=['POST'])
user_blueprint.add_url_rule('/login', view_func=UserLoginView.as_view('login_view'), methods=['POST'])
user_blueprint.add_url_rule('/<int:user_id>/profile', view_func=UserProfileView.as_view('user_profile'), methods=['GET'])
