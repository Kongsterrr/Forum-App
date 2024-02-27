import datetime
from typing import Optional

import jwt

import config
from aop.exceptions import *
from models.user import User
from repos.user_repo import UserRepository
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError
import requests



class UserService:
    def __init__(self):
        self.user_repository = UserRepository()  # it's better to use dependency injection here

    def get_user(self, userId: int) -> Optional[User]:
        u: User = self.user_repository.get_user_by_Id(userId)
        if u is None:
            raise NotFoundException('User not found')
        return u

    def create_user(self, user_data):
        try:
            new_user = User(**user_data)
            success, message = self.user_repository.add_user(new_user)
            return success, message
        except IntegrityError as e:
            raise DuplicateEmailException("This email is already registered.")
        except Exception as e:
            raise

    def get_user_token_and_type(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if user and password:
            # token: str = jwt.encode(
            #     {'user_id': user.userId, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
            #     config.JWT_SECURITY_KEY, "HS256")
            # return token, user.type
            auth_service_url = "http://127.0.0.1:5000/authentication/register"
            payload = {
                'user_id': user.userId
            }
            response = requests.post(auth_service_url, json=payload)
            if response.status_code == 200:
                data = response.json()
                token = data.get('token')
                user_status = data.get('user_status')
                return token, user_status

        raise NotFoundException('User not found')

    def get_user_profile(self, user_id):
        user = self.user_repository.get_user_by_Id(user_id)
        if not user:
            raise NotFoundException('User not found')

        return {
            "profileImage": user.profileImageURL,
            "firstName": user.firstName,
            "lastName": user.lastName,
            "dateJoined": user.dateJoined.strftime('%Y-%m-%d')
        }
