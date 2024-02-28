from flask import Blueprint
from controllers.auth_controller import SendEmailView, UserLoginView, UserRegisterView

auth_blueprint = Blueprint('authentication', __name__, url_prefix='/authentication')
auth_blueprint.add_url_rule('/register', view_func=UserRegisterView.as_view('auth-register'), methods=['POST'])
auth_blueprint.add_url_rule('/login', view_func=UserLoginView.as_view('auth-login'), methods=['POST'])
auth_blueprint.add_url_rule('/email/send', view_func=SendEmailView.as_view('auth-email-send'), methods=['POST'])

