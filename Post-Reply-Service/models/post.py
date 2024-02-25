from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, Text
from sqlalchemy.sql import func


class Post(Base):
    __tablename__ = 'Post'

    postId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    isArchived = Column(Boolean, nullable=False)
    status = Column(String(50), nullable=False)
    dateCreated = Column(DateTime, default=func.now())
    dateModified = Column(DateTime)
    images = Column(JSON)
    attachments = Column(JSON)