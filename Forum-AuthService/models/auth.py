from .database import Base
from sqlalchemy import Column, Integer, String


class Auth(Base):
    __tablename__ = 'user_auth'

    userId = Column(Integer, primary_key=True)
    token = Column(String(80), nullable=True)
    verification_code = Column(String(80), nullable=True)
    status = Column(String(50), nullable=True)
    