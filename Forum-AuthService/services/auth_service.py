import pika

class AuthService:
    def __init__(self):
        pass

    def send_email_to_queue(self, receiver_email):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='email_queue')
        message = f'{receiver_email}'
        channel.basic_publish(exchange='', routing_key='email_queue', body=message)

        print("Message sent to RabbitMQ queue")

        connection.close()
        return {"message": "User email sent to RabbitMQ queue."}