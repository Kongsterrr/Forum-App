import datetime
import random
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
            success, message, user_id = self.user_repository.add_user(new_user)
            return success, message, user_id
        except IntegrityError as e:
            return False, str("This email is already registered."), None
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

        # return {
        #     "profileImage": user.profileImageURL,
        #     "firstName": user.firstName,
        #     "lastName": user.lastName,
        #     "dateJoined": user.dateJoined.strftime('%Y-%m-%d')
        # }
        return user

    def generate_verification_code(self):
        return str(random.randint(100000, 999999))
    
    def send_verification_code(self, user_id):

        verification_code = self.generate_verification_code()

        # connect to db, update user verification code

        user_email = self.user_repository.get_email_by_user(user_id)
        self.user_repository.set_user_verification(user_id, verification_code)

        auth_service_url = "http://127.0.0.1:5000/authentication/email/send"
        payload = {
            'user_email': user_email,
            'verification_code': verification_code
        }

        response = requests.post(auth_service_url, json=payload)
    
        if response.status_code == 200:
            return {"Message": "Email sent to the user."}
        else:
            return {"Message": "Failure, check email validity."}

    def authenticate_user(self, user_email, password):
        return self.user_repository.authenticate_user(user_email, password)

    def verify_user(self, user_id, verification_code):
        saved_code = self.user_repository.get_verification_code_by_id(user_id)
        if saved_code and saved_code == verification_code:
            # Modify user status in db
            self.user_repository.set_user_status(user_id, "Normal-write")

            # Return new token?
            return True
        else:
            return False

    def upgrade_to_admin(self, userId, user_status):
        if user_status != "SuperAdmin":
            return False, "Only SuperAdmin can upgrade Normal User to Admin User"
        return self.user_repository.upgrade_user_to_admin(userId)
    
    def update_profile_pic(self, user_id, pic_path):
        auth_service_url = "http://127.0.0.1:5000/file/upload"
        payload = {
            'user_id': user_id,
            'file_path': pic_path
        }
        response = requests.post(auth_service_url, json=payload)
    
        if response.status_code == 200:
            # save url to db
            data = response.json()
            url = data.get('url')
            self.user_repository.update_user_profile_pic(user_id, url)
            return {"Message": "Successfully set user profile picture."}
        else:
            return {"Message": "Picture update failure."}
    
    def update_user_email(self, user_id, user_email):
        self.user_repository.update_user_email(user_id, user_email)
        self.send_verification_code(user_id)
        return {"Message": "Email sent to the user for update."}

    def update_user_profile(self, user_id, profile_data):

        response = {}

        if 'email' in profile_data:
            response['email_update'] = self.update_user_email(user_id, profile_data['email'])
        
        elif 'profileImageURL' in profile_data:
            response['profileImageURL_update'] =self.update_profile_pic(user_id, profile_data['profileImageURL'])
        
        elif 'firstName' in profile_data:
            response['firstName_update'] = self.user_repository.update_user_firstname(user_id, profile_data['firstName'])

        elif 'lastName' in profile_data:
            response['lastName_update'] = self.user_repository.update_user_lastname(user_id, profile_data['lastName'])
        
        return response

    def get_all_user(self, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to view all users."
        all_users = self.user_repository.get_all_user_repo()
        return True, all_users

    def ban_user(self, userId, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to ban this users."
        banned_user = self.user_repository.ban_user_repo(userId)
        return True, banned_user

    def unban_user(self, userId, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to unban this users."
        unbanned_user = self.user_repository.unban_user_repo(userId)
        return True, unbanned_user


    

