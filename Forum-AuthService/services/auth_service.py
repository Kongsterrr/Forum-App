import pika

class AuthService:
    def __init__(self, rabbitmq_host='localhost'):

        self.rabbitmq_host = rabbitmq_host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbitmq_host))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='verification_code_queue')
        self.channel.queue_declare(queue='email_queue')
        self.channel.basic_consume(queue='verification_code_queue', on_message_callback=self.process_verification_code, auto_ack=True)

        # self.start_listening()

    def process_verification_code(self, ch, method, properties, body):
        data = body.decode('utf-8').split(',')
        receiver_email, verification_code = data[0], data[1]
        print("Received verification code:")
        print("Receiver Email:", receiver_email)
        print("Verification Code:", verification_code)

    def start_listening(self):
        print('Auth service started listening for verification codes from RabbitMQ...')
        self.channel.start_consuming()

    def send_email_to_queue(self, receiver_email):

        message = f'{receiver_email}'
        self.channel.basic_publish(exchange='', routing_key='email_queue', body=message)
        print("Message sent to RabbitMQ queue")

        return {"message": "User email sent to RabbitMQ queue."}