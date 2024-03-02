from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'messages'

    messageId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(10), nullable=False)

    def __init__(self, userId, email, message, dateCreated, status):
        self.userId = userId
        self.email = email
        self.message = message
        self.dateCreated = dateCreated
        self.status = status
