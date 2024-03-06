from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func



class History(Base):
    __tablename__ = 'History'

    historyId = Column(Integer, primary_key=True)
    userId = Column(Integer, nullable=False)
    postId = Column(Integer, nullable=False)
    viewDate = Column(DateTime, default=func.now())

    def serialize(self):
        return {
                'historyId': self.historyId,
                'userId': self.userId,
                'postId': self.postId,
                'viewDate': self.viewDate
                }