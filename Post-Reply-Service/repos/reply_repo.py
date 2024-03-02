from typing import Optional

from aop.exceptions import NotFoundException
from models.reply import Reply
from models.database import db


class ReplyRepository:

    def add_reply(self, reply: Reply):
        db.add(reply)
        try:
            db.commit()
            return True, "Reply added successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)

    def get_by_id(self, id: int) -> Optional[Reply]:
        return db.query(Reply).get(id)

    def get_by_post_id(self, post_id: int) -> Optional[Reply]:
        return db.query(Reply).filter(Reply.postId == post_id).all()
