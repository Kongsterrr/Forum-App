from flask import jsonify
from .exceptions import AuthorizationError, RequestDataError, InvalidTokenError

def handle_authorization_error(e):
    return jsonify({'error': str(e)}), 401

def handle_request_data_error(e):
    return jsonify({'error': str(e)}), 400

def handle_invalid_token_error(e):
    return jsonify({'error': str(e)}), 401

def initialize_error_handlers(app):
    app.register_error_handler(AuthorizationError, handle_authorization_error)
    app.register_error_handler(RequestDataError, handle_request_data_error)
    app.register_error_handler(InvalidTokenError, handle_invalid_token_error)