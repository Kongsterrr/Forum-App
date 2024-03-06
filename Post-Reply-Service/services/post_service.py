import datetime
from typing import Optional

import jwt
import requests

import config
from aop.exceptions import *
from models.post import Post
from repos.post_repo import PostRepository
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError

class PostService:
    def __init__(self):
        self.post_repository = PostRepository()  # it's better to use dependency injection here
        self.file_service_url = 'http://127.0.0.1:5000/file/'

    def get_post(self, post_id):
        post = self.post_repository.get_post_by_Id(post_id)
        if post is None:
            raise NotFoundException('Post not found')
        return post
    
    def upload_files_to_S3(self, file_paths, user_id):

        query_url = self.file_service_url + 'upload-files'

        payload ={
            'user_id': user_id,
            'file_paths': file_paths
        }

        response = requests.post(query_url, json=payload)

        if response.status_code == 200:
            data = response.json()
            urls = data.get('urls')
            print("post get urls: ", urls)
            return {'urls': urls}
        else:
            raise NotFoundException('Post Created Failed: files upload failure')

    def create_post_published(self, post_data, user_id):
        try:
            # post_data['status'] = 'Published'
            post_data['userId'] = user_id


            # Upload images or attachments to S3 bucket
            if 'images' in post_data:
                images = post_data['images']
                url_json = self.upload_files_to_S3(images, user_id)
                if url_json:
                    post_data['images'] = url_json
                else:
                    raise NotFoundException('Post Created Failed: files upload failure')
                
            new_post = Post(**post_data)
            success, message = self.post_repository.add_post(new_post)
            return success, message
        except Exception as e:
            raise NotFoundException('Post Created Failed')

    def update_post(self, post_id, post_data, user_id):
        post = self.post_repository.get_post_by_Id(post_id)
        if post.userId != user_id:
            return False, "User is not authorized to update this post"
        try:
            post_data['userId'] = user_id

            if 'images' in post_data:
                images = post_data['images']
                url_json = self.upload_files_to_S3(images, user_id)
                if url_json:
                    post_data['images'] = url_json
                else:
                    raise NotFoundException('Post Update Failed: files upload failure')

            success, message = self.post_repository.update_post_repo(post_id, post_data)
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

    def get_delete_post(self, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to view all the deleted post."
        deleted_posts = self.post_repository.get_all_deleted_post()
        return True, deleted_posts

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
            raise NotFoundException

    # For Admin
    def get_ban_post(self, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions view all the banned post."
        ban_posts = self.post_repository.get_all_banned_post()
        return True, ban_posts


    def ban_post(self, post_id, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to ban the post."
        try:
            success, message = self.post_repository.mark_post_to_banned(post_id)
            return success, message
        except Exception as e:
            raise NotFoundException

    # For Admin
    def unbanned_post(self, post_id, user_status):
        if user_status != "Admin":
            return False, "Insufficient permissions to unban the post."
        try:
            success, message = self.post_repository.unbanned_post_to_published(post_id)
            return success, message
        except Exception as e:
            raise NotFoundException

    def fetch_published_posts(self):
        return self.post_repository.get_published_posts()

    def get_top_user_posts(self, user_id):
        return self.post_repository.get_top_posts_by_user(user_id)


    def get_unpublished_posts(self, user_id):
        return self.post_repository.get_unpublished_posts_by_user(user_id)

    def get_hidden_post(self, user_id):
        return self.post_repository.get_hidden_posts_by_user(user_id)





