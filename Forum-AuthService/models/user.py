from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func



class User(Base):
    __tablename__ = 'User'

    userId = Column(Integer, primary_key=True)
    firstName = Column(String(80), nullable=False)
    lastName = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    active = Column(Boolean, default=True)
    dateJoined = Column(DateTime, default=func.now())
    profileImageURL = Column(String(128))
    type = Column(String(80), default="Normal")
    verificationCode = Column(String(80), nullable=True)

    def serialize(self):
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
        }
