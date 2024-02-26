from typing import Optional

from aop.exceptions import NotFoundException
from models.post import Post
from models.database import db


class PostRepository:
    def get_post_by_Id(self, postId):
        return db.query(Post).get(postId)

    def add_post(self, new_post):
        db.add(new_post)
        try:
            db.commit()
            return True, "Post added successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)

    def update_post(self, post_id, post_data):
        post = db.query(Post).filter_by(postId=post_id).first()
        if post:
            for key, value in post_data.items():
                setattr(post, key, value)
            db.commit()
            return True, "Post updated successfully."
        return False, "Post not found."


    def mark_post_as_published(self, post_id):
        post = db.query(Post).filter_by(postId=post_id).first()
        if post and (post.status == "Unpublished" or post.status == "Hidden"):
            post.status = "Published"
            db.commit()
            return True, "Post marked as Published."
        return False, "Post not found or insufficient permissions."

    def change_post_visibility(self, post_id):
        post = db.query(Post).filter_by(postId=post_id).first()
        if post and post.status == "Published":
            post.status = "Hidden"
            db.commit()
            return True, "Post marked as Hidden"
        return False, "Post not found or insufficient permissions."

    def mark_post_as_deleted(self, post_id):
        post = db.query(Post).filter_by(postId=post_id).first()
        if post and post.status == "Published":
            post.status = 'Deleted'
            db.commit()
            return True, "Post marked as Deleted."
        return False, "Post not found or insufficient permissions."

    def change_post_archived_status(self, post_id):
        post = db.query(Post).filter_by(postId=post_id).first()
        if post and post.status == "Published":
            post.isArchived = True
            db.commit()
            return True, "Post archived status updated."
        return False, "Post not found or insufficient permissions."
