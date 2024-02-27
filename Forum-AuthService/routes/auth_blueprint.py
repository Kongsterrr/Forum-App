from flask import Blueprint
from controllers.auth_controller import CodeVerifyView, SendEmailView, TokenVerifyView, UserRegisterView

auth_blueprint = Blueprint('authentication', __name__, url_prefix='/authentication')
auth_blueprint.add_url_rule('/register', view_func=UserRegisterView.as_view('auth-register'), methods=['POST'])
auth_blueprint.add_url_rule('/email/send', view_func=SendEmailView.as_view('auth-email-send'), methods=['POST'])
auth_blueprint.add_url_rule('/email/verify', view_func=CodeVerifyView.as_view('auth-email'), methods=['POST'])
auth_blueprint.add_url_rule('/token/verify', view_func=TokenVerifyView.as_view('auth-token'), methods=['POST'])
