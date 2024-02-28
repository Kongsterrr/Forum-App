from typing import Optional

from models.user import User
from models.database import db


class UserRepository:
    def get_user_by_Id(self, userId) -> Optional[User]:
        return db.query(User).get(userId)

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
    
    def authenticate_user(self, email, password):
        this_user = self.get_user_by_email(email)
        if password == this_user.password:
            return this_user.userId
        else:
            return None
    
    def get_user_type(self, user_id):
        return self.get_user_by_Id(user_id).type