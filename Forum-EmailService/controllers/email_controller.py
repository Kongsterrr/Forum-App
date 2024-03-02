from flask import jsonify, request
from flask.views import MethodView

from services.email_service import EmailService


class EmailView(MethodView):

    def __init__(self, app):
        self.email_service = EmailService(app)  

    def post(self):  
        data = request.get_json()
        
        if 'receiver_email' not in data:
            return jsonify({'error': 'Receiver email not provided'}), 400

        receiver_email = data['receiver_email']

        result = self.email_service.send_verification_code(receiver_email)
        return jsonify(result)

        



