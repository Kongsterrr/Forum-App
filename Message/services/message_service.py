from datetime import datetime

from models.message import Message, db
from repos.message_repo import MessageRepository

class MessageService:
    def __init__(self):
        self.message_repository = MessageRepository()

    def create_message(self, user_id, message_data):
        message = message_data.get('message')
        email = message_data.get('email')
        date_created = datetime.utcnow()
        status = 'Open'

        result = self.message_repository.save_message(user_id, email, message, date_created, status)
        return result

    def get_all_messages(self):
        messages = Message.query.all()
        # Serialize the messages to a list of dictionaries
        serialized_messages = [{
            'messageId': message.messageId,
            'userId': message.userId,
            'email': message.email,
            'message': message.message,
            'dateCreated': message.dateCreated.strftime('%Y-%m-%d %H:%M:%S'),
            'status': message.status
        } for message in messages]
        return serialized_messages

    def update_message_status(self, messageId, status):
        message = Message.query.get(messageId)
        if not message:
            return {'error': 'Message not found'}, 404

        message.status = status
        db.session.commit()

        return {'message': 'Message status updated successfully'}, 200