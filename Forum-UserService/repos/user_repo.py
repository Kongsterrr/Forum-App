from typing import Optional

from aop.exceptions import NotFoundException
from models.user import User
from models.database import db


class UserRepository:
    def get_user_by_Id(self, userId) -> Optional[User]:
        return db.query(User).get(userId)
        # if user_id == 1:
        #     return User(1, 'kason', 'kason@gmail.com')
        # else:
        #     return None

    def add_user(self, new_user):
        db.add(new_user)
        try:
            db.commit()
            return True, "User registered successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)

    def get_user_by_email(self, email):
        return db.query(User).filter_by(email=email).first()
    
    def get_email_by_user(self, user_id):
        return self.get_user_by_Id(user_id).email
    
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


