from typing import Optional

from aop.exceptions import NotFoundException
from models.post import Post
from models.database import db


class PostRepository:
    def get_post_by_Id(self, postId):
        return db.query(Post).get(postId)