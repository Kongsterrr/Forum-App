import datetime
from typing import Optional

import jwt

import config
from aop.exceptions import *
from models.post import Post
from repos.post_repo import PostRepository
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError

class PostService:
    def __init__(self):
        self.post_repository = PostRepository()  # it's better to use dependency injection here

    def get_post(self, postId: int):
        post = self.post_repository.get_post_by_Id(postId)
        if post is None:
            raise NotFoundException('Post not found')
        return post
