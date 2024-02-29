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

    def get_post(self, post_id):
        post = self.post_repository.get_post_by_Id(post_id)
        if post is None:
            raise NotFoundException('Post not found')
        return post

    def create_post_published(self, post_data, user_id):
        try:
            # post_data['status'] = 'Published'
            post_data['userId'] = user_id
            new_post = Post(**post_data)
            success, message = self.post_repository.add_post(new_post)
            return success, message
        except Exception as e:
            raise NotFoundException('Post Created Failed')

    def update_post(self, post_id, post_data):
        try:
            success, message = self.post_repository.update_post(post_id, post_data)
            return success, message
        except Exception as e:
            raise NotFoundException('Post Updated Failed')

    def publish_post(self, post_id, user_id):
        post = self.post_repository.get_post_by_Id(post_id)
        if post.userId != user_id:
            return False, "User is not authorized to publish this post"
        try:
            success, message = self.post_repository.mark_post_as_published(post_id)
            return success, message
        except Exception as e:
            raise NotFoundException('Post Published Failed')

    def hide_post(self, post_id, user_id):
        post = self.post_repository.get_post_by_Id(post_id)
        if post.userId != user_id:
            return False, "User is not authorized to hide this post"
        try:
            success, message = self.post_repository.change_post_visibility(post_id)
            return success, message
        except Exception as e:
            raise NotFoundException('Post Hided Failed')

    def delete_post(self, post_id, user_id):
        post = self.post_repository.get_post_by_Id(post_id)
        if post.userId != user_id:
            return False, "User is not authorized to delete this post"
        try:
            success, message = self.post_repository.mark_post_as_deleted(post_id)
            return success, message
        except Exception as e:
            raise NotFoundException('Post Deleted Failed')

    def archive_post(self, post_id, user_id):
        post = self.post_repository.get_post_by_Id(post_id)
        if post.userId != user_id:
            return False, "User is not authorized to delete this post"
        try:
            success, message = self.post_repository.change_post_archived_status(post_id)
            return success, message
        except Exception as e:
            raise NotFoundException('Post Archived Failed')

    # For Admin
    def recover_post(self, post_id, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to recover the post."
        try:
            success, message = self.post_repository.recover_deleted_post_to_published(post_id)
            return success, message
        except Exception as e:
            raise NotFoundExcept

    # For Admin
    def ban_post(self, post_id, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to ban the post."
        try:
            success, message = self.post_repository.mark_post_to_banned(post_id)
            return success, message
        except Exception as e:
            raise NotFoundExcept

    # For Admin
    def unbanned_post(self, post_id, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to unban the post."
        try:
            success, message = self.post_repository.unbanned_post_to_published(post_id)
            return success, message
        except Exception as e:
            raise NotFoundExcept

    def fetch_published_posts(self):
        return self.post_repository.get_published_posts()

    def get_top_user_posts(self, user_id):
        return self.post_repository.get_top_posts_by_user(user_id)


    def get_unpublished_posts(self, user_id):
        return self.post_repository.get_unpublished_posts_by_user(user_id)




