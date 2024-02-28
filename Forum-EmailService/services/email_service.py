from flask_mail import Message, Mail
import random
import pika

class EmailService:
    def __init__(self, app):
        self.mail = Mail(app)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='email_queue')
        self.channel.basic_consume(queue='email_queue', on_message_callback=self.send_verification_code, auto_ack=True)

        # self.channel.queue_declare(queue='verification_code_queue')

        self.start_listening()

    # def generate_verification_code(self):
    #     return str(random.randint(100000, 999999))

    def send_verification_code(self, ch, method, properties, body):
        data = body.decode('utf-8').split(',')
        receiver_email = data[0]
        verification_code = data[1]
        
        msg = Message('Verification Code', sender="azure.hrj@gmail.com", recipients=[receiver_email])
        msg.body = f'Your verification code is: {verification_code}'

        try:
            self.mail.send(msg)
            print('Verification code sent successfully')
            # message_to_queue = f'{user_id},{verification_code}'
            # self.channel.basic_publish(exchange='', routing_key='verification_code_queue', body=message_to_queue)
            # print('Verification code published to verification_code_queue')
        except Exception as e:
            print(f'Error sending verification code: {str(e)}')

    def start_listening(self):
        print('Email service started listening for messages from RabbitMQ...')
        self.channel.start_consuming()

    def stop_listening(self):
        self.connection.close()