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

    def get_reply_by_id(self, reply_id):
        reply = self.reply_repository.get_by_id(reply_id)
        if reply is None:
            raise NotFoundException('Reply not found')
        return reply

    def get_all_replies_by_user(self, user_id):
        return self.reply_repository.get_by_user_id(user_id)

    def get_all_replies_by_post(self, post_id):
        return self.reply_repository.getpost_by_post_id(post_id)


