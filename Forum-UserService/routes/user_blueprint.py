from flask import Blueprint

from controllers.user_controller import UserEmailVerificationView, UserRegisterView, UserLoginView, UserProfileView, UserStatusUpgradeView, UserProfileUpdateView, AdminAllUserProfileView, BanUserView, UnBanUserView

user_blueprint = Blueprint('users', __name__, url_prefix='/users')
# user_blueprint.add_url_rule('/<int:user_id>', view_func=UserView.as_view('user'), methods=['GET', 'PUT'])
user_blueprint.add_url_rule('/register', view_func=UserRegisterView.as_view('register_view'), methods=['POST'])
user_blueprint.add_url_rule('/authenticate', view_func=UserLoginView.as_view('login_view'), methods=['POST'])
user_blueprint.add_url_rule('/profile', view_func=UserProfileView.as_view('user_profile'), methods=['GET'])
user_blueprint.add_url_rule('/email', view_func=UserEmailVerificationView.as_view('send-email'), methods=['GET', 'POST'])
user_blueprint.add_url_rule('/upgrade/<int:userId>', view_func=UserStatusUpgradeView.as_view('upgrade-admin'), methods=['PUT'])
user_blueprint.add_url_rule('/profile/update/<int:user_id>', view_func=UserProfileUpdateView.as_view('user-update'), methods=['POST'])
user_blueprint.add_url_rule('/all', view_func=AdminAllUserProfileView.as_view('all_users'), methods=['GET'])
user_blueprint.add_url_rule('/ban/<int:userId>', view_func=BanUserView.as_view('ban_user'), methods=['PUT'])
user_blueprint.add_url_rule('/unban/<int:userId>', view_func=UnBanUserView.as_view('unban_user'), methods=['PUT'])

