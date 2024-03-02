import datetime

import requests
import config
import pika
import jwt
from aop.exceptions import *


class AuthService:
    def __init__(self, rabbitmq_host='localhost'):

        self.rabbitmq_host = rabbitmq_host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbitmq_host))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='email_queue')
    
    def create_user(self, user_data):

        user_service_url = "http://127.0.0.1:5000/users/register"
    
        response = requests.post(user_service_url, json=user_data)
        data = response.json()
        message = data.get('message')
        user_id = data.get('user_id')

        if response.status_code == 201:
            return True, message, user_id

        else:
            return False, message, user_id
    
    def login_user(self, user_email, password):

        user_service_url = "http://127.0.0.1:5000/users/authenticate"
        payload = {
            'email': user_email,
            'password': password
        }

        response = requests.post(user_service_url, json=payload)
        data = response.json()
        auth_status = data.get('Authentication status')

        if auth_status == 'Success':
            user_id = data.get('user_id')
            user_status = data.get('user_status')
            token = self.generate_user_token(user_id, user_status)
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
