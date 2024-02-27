from typing import Optional

from models.auth import Auth
from models.database import db


class AuthRepository:

    def add_user(self, user_id):
        new_auth_model = Auth(userId=user_id)
        db.add(new_auth_model)
        try:
            db.commit()
            return True, "User registered in authentication system successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)
    
    def set_auth_token(self, user_id, token):
        auth_model = db.query(Auth).filter_by(userId=user_id).first()
        if auth_model:
            auth_model.token = token
            db.commit()
            return True
        return False

    def set_verification_code(self, user_id, verification_code):
        auth_model = db.query(Auth).filter_by(userId=user_id).first()
        if auth_model:
            auth_model.verification_code = verification_code
            db.commit()
            return True
        return False

    def get_token_by_user_id(self, user_id):
        auth_model = db.query(Auth).filter_by(userId=user_id).first()
        if auth_model:
            return auth_model.token
        return None

    def get_verification_code_by_user_id(self, user_id):
        auth_model = db.query(Auth).filter_by(userId=user_id).first()
        if auth_model:
            return auth_model.verification_code
        return None

    def set_user_status(self, user_id, user_status):
        auth_model = db.query(Auth).filter_by(userId=user_id).first()
        if auth_model:
            auth_model.status = user_status
            db.commit()
            return True
        return None
