import datetime
import config
import pika
import jwt
from aop.exceptions import *
from repos.auth_repo import AuthRepository
from repos.user_repo import UserRepository
from models.auth import Auth
from models.user import User
from sqlalchemy.exc import IntegrityError


class AuthService:
    def __init__(self, rabbitmq_host='localhost'):

        self.auth_repository = AuthRepository()
        self.user_repository = UserRepository()

        self.rabbitmq_host = rabbitmq_host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbitmq_host))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='email_queue')
    
    def create_user(self, user_data):
        try:
            new_user = User(**user_data)
            success, message = self.user_repository.add_user(new_user)
            return success, message
        except IntegrityError as e:
            raise DuplicateEmailException("This email is already registered.")
        except Exception as e:
            raise
    
    def login_user(self, user_email, password):
        user_id = self.user_repository.authenticate_user(user_email, password)
        if user_id:
            current_status = self.user_repository.get_user_type(user_id)
            token = self.generate_user_token(user_id, current_status)
            return {"login status": "Success", "token": token}
        else:
            return {"login status": "Failure", "token": None}
        

    def send_email_to_queue(self, receiver_email, verification_code):
        message = f'{receiver_email}, {verification_code}'
        self.channel.basic_publish(exchange='', routing_key='email_queue', body=message)
        print("Message sent to RabbitMQ queue")

        return {"message": "User email sent to RabbitMQ queue."}
       

    def generate_user_token(self, user_id, user_status):
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=10000)
        token_payload = {'user_id': user_id, 'user_status': user_status, 'exp': expiration_time}
        jwt_secret_key = config.JWT_SECURITY_KEY
        token = jwt.encode(token_payload, jwt_secret_key, algorithm="HS256")
        return token
