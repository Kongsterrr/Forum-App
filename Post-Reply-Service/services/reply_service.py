import datetime
from typing import Optional

import jwt

import config
from aop.exceptions import *
from models.reply import Reply
from repos.reply_repo import ReplyRepository
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError

class ReplyService:
    def __init__(self):
        self.reply_repository = ReplyRepository()

    def create_reply(self, reply_data):
        try:
            new_reply = Reply(**reply_data)
            success, message = self.reply_repository.add_reply(new_reply)
            return success, message
        except Exception as e:
            raise