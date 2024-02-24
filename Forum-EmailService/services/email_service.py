from flask_mail import Message, Mail
import random

class EmailService:
    def __init__(self, app):
        self.mail = Mail(app)

    def generate_verification_code(self):
        return str(random.randint(100000, 999999))

    def send_verification_code(self, receiver_email):
        verification_code = self.generate_verification_code()
        msg = Message('Verification Code', sender="azure.hrj@gmail.com", recipients=[receiver_email])
        msg.body = f'Your verification code is: {verification_code}'

        try:
            self.mail.send(msg)
            return {'message': 'Verification code sent successfully'}
        except Exception as e:
            return {'error': str(e)}