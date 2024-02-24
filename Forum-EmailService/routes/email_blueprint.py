from flask import Blueprint, current_app
from controllers.email_controller import EmailView

email_blueprint = Blueprint('email', __name__)
email_blueprint.add_url_rule('/email/verify', view_func=EmailView.as_view('email-verify', current_app), methods=['POST'])