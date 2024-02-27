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


