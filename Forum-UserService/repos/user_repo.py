from typing import Optional

from pymysql import IntegrityError

from aop.exceptions import NotFoundException
from models.user import User
from models.database import db


class UserRepository:
    def get_user_by_Id(self, userId) -> Optional[User]:
        return db.query(User).get(userId)

    def add_user(self, new_user):
        db.add(new_user)
        try:
            db.commit()
            user_id = self.get_user_by_email(new_user.email).userId
            return True, "User registered successfully.", user_id
        except IntegrityError as e:
            db.rollback()
            return False, str(e), None

    def get_user_by_email(self, email):
        return db.query(User).filter_by(email=email).first()
    
    def get_email_by_user(self, user_id):
        return self.get_user_by_Id(user_id).email
    
    def authenticate_user(self, email, password):
        this_user = self.get_user_by_email(email)
        print("this_user email: ", this_user.email)
        print("this_user password: ", this_user.password)
        print("input password: ", password)
        if password == this_user.password:
            return this_user.userId, this_user.type
        else:
            return None, None

    
    def set_user_verification(self, user_id, verification_code):
        user_model = db.query(User).get(user_id)
        user_model.verificationCode = verification_code
        try:
            db.commit()
            return True, "User verification code set successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)
    
    def get_verification_code_by_id(self, userId):
        user_model = self.get_user_by_Id(userId)
        return user_model.verificationCode
    
    def set_user_status(self, userId, user_status):
        user_model = self.get_user_by_Id(userId)
        user_model.type = user_status
        try:
            db.commit()
            return True, "User status set successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)
    
    def update_user_email(self, userId, user_email):
        user_model = self.get_user_by_Id(userId)
        user_model.email = user_email
        try:
            db.commit()
            return True, "User email updated successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)
    
    def update_user_profile_pic(self, userId, url):
        user_model = db.query(User).get(userId)
        user_model.profileImageURL = url
        try:
            db.commit()
            return True, "User profile image set successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)
    
    def update_user_firstname(self, userId, firstName):
        user_model = db.query(User).get(userId)
        user_model.firstName = firstName
        try:
            db.commit()
            return True, "User firstname set successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)
    
    def update_user_lastname(self, userId, lastName):
        user_model = db.query(User).get(userId)
        user_model.lastName = lastName
        try:
            db.commit()
            return True, "User lastname set successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)

    def upgrade_user_to_admin(self, userId):
        user = db.query(User).get(userId)
        print(user.type)
        if user and (user.type == "Normal" or user.type == "Normal-write"):
            user.type = 'Admin'
            db.commit()
            return True, f"User {user.email} upgraded to admin."
        return False, "User not found."

    def get_all_user_repo(self):
        all_users = db.query(User).all()
        return all_users

    def ban_user_repo(self, userId):
        user = db.query(User).get(userId)
        if user and user.type == "Normal" and user.active == True:
            user.active = False
            db.commit()
            return True, f"User {user.email} banned successfully."
        return False, "User not found."

    def unban_user_repo(self, userId):
        user = db.query(User).get(userId)
        if user and user.type == "Normal" and user.active == False:
            user.active = True
            db.commit()
            return True, f"User {user.email} unbanned successfully."
        return False, "User not found."



