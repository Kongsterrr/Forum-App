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

    # For Admin
    def recover_deleted_post_to_published(self, post_id):
        post = db.query(Post).filter_by(postId=post_id).first()
        if post and post.status == "Deleted":
            post.status = 'Published'
            db.commit()
            return True, "Recover Delete Post to Published"
        return False, "Post not found or insufficient permissions."

    # For Admin
    def mark_post_to_banned(self, post_id):
        post = db.query(Post).filter_by(postId=post_id).first()
        if post and post.status == "Published":
            post.status = 'Banned'
            db.commit()
            return True, "Successfully Banned Post"
        return False, "Post not found or insufficient permissions."

    # For Admin
    def unbanned_post_to_published(self, post_id):
        post = db.query(Post).filter_by(postId=post_id).first()
        if post and post.status == "Banned":
            post.status = 'Published'
            db.commit()
            return True, "Successfully UnBanned Post to Published"
        return False, "Post not found or insufficient permissions."


    def get_published_posts(self):
        return db.query(Post).filter_by(status='Published').order_by(Post.dateCreated.desc()).all()