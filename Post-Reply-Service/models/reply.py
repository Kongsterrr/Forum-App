from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func


class Reply(Base):
    __tablename__ = 'Reply'

    replyId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, nullable=False)
    postId = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    isActive = Column(Boolean, default=True)
    dateCreated = Column(DateTime, default=func.now())

    def serialize(self):
        return {
            'replyId': self.replyId,
            'userId': self.userId,
            'postId': self.postId,
            'comment': self.comment,
            'isActive': self.isActive,
            'dateCreated': self.dateCreated
        }