from app import db
from models.message import Message

class MessageRepository:
    def save_message(self, user_id, email, message, date_created, status):
        new_message = Message(userId=user_id, email=email, message=message, dateCreated=date_created, status=status)
        db.session.add(new_message)
        db.session.commit()
        return {'message': 'Message saved successfully.'}