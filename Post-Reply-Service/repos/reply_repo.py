from typing import Optional

from aop.exceptions import NotFoundException
from models.reply import Reply
from models.database import db


class ReplyRepository:
    def get_by_id(self, id: int) -> Optional[Reply]:
        return db.session.query(Reply).filter(Reply.id == id)