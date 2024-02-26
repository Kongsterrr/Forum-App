from flask import Blueprint
from controllers.auth_controller import AuthView

auth_blueprint = Blueprint('auth', __name__)
auth_blueprint.add_url_rule('/auth/email', view_func=AuthView.as_view('auth-email'), methods=['POST'])