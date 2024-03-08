import datetime
from typing import Optional
import jwt
from aop.exceptions import NotFoundException
from flask import request, jsonify
import requests

class PostHistoryService:
    def __init__(self):
        self.history_url = 'http://127.0.0.1:5000/history'
        self.post_reply_url = 'http://127.0.0.1:5000/post_and_reply'
        self.user_service_url = 'http://127.0.0.1:5000/users'


    def get_post_history(self, user_id):
        history_response = requests.get(self.history_url + '/' + str(user_id))
        histories = history_response.json()["histories"]

        post_history = []
        for history in histories:
            post_response = requests.get(self.post_reply_url + '/' + str(history["postId"]))
            post = post_response.json()
            if "postId" not in post:
                continue
            print(post)

            userId = post["userId"]
            user_response = requests.get(self.user_service_url + '/' + str(userId))
            user = user_response.json()
            post["firstName"] = user["firstName"]
            post["lastName"] = user["lastName"]
            post["dateViewed"] = history["viewDate"]
            post_history.append(post)
        post_history.sort(key=lambda x: x["dateViewed"])
        return post_history
