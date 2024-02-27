from flask import Blueprint
from controllers.auth_controller import CodeVerifyView, SendEmailView, TokenVerifyView, UserRegisterView

auth_blueprint = Blueprint('auth', __name__)
auth_blueprint.add_url_rule('/auth/register', view_func=UserRegisterView.as_view('auth-register'), methods=['POST'])
auth_blueprint.add_url_rule('/auth/email/send', view_func=SendEmailView.as_view('auth-email-send'), methods=['POST'])
auth_blueprint.add_url_rule('/auth/email/verify', view_func=CodeVerifyView.as_view('auth-email'), methods=['POST'])
auth_blueprint.add_url_rule('/auth/token/verify', view_func=TokenVerifyView.as_view('auth-token'), methods=['POST'])
