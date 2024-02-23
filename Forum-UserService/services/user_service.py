import datetime
from typing import Optional

import jwt

import config
from aop.exceptions import *
from models.user import User
from repos.user_repo import UserRepository
from werkzeug.security import check_password_hash



class UserService:
    def __init__(self):
        self.user_repository = UserRepository()  # it's better to use dependency injection here

    def get_user(self, userId: int) -> Optional[User]:
        u: User = self.user_repository.get_user_by_Id(userId)
        if u is None:
            raise NotFoundException('User not found')
        return u

    def create_user(self, request):
        try:
            new_user = User(**request.json)
            success, message = self.user_repository.add_user(new_user)
            return success, message
        except Exception as e:
            raise DuplicateEmailException("This email is already registered.")

    def get_user_token(self, email: str, password: str) -> Optional[str]:
        user: User = self.user_repository.get_user_by_email(email)
        if user and check_password_hash(user.password, password):
            token: str = jwt.encode(
                {'user_id': user.userId, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
                config.JWT_SECURITY_KEY, "HS256")
            return token

        raise NotFoundException('User not found')
