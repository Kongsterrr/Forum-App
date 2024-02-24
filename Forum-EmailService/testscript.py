import pika

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='email_queue')

# Send a message to the queue
receiver_email = 'ruijiehuang98@gmail.com'
message = f'{receiver_email}'
channel.basic_publish(exchange='', routing_key='email_queue', body=message)

print("Message sent to RabbitMQ queue")

# Close the connection
connection.close()
