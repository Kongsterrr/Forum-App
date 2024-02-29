import datetime
from typing import Optional
import jwt
from aop.exceptions import NotFoundException
from flask import request
import requests

class PostHistoryService:
    def __init__(self):
        self.history_url = 'http://127.0.0.1:5000/history'
        self.post_reply_url = 'http://127.0.0.1:5000/post_and_reply'

    # def get_post_history(self, post_id):
    #     history_response = requests.get(self.history_url + '/' +)

# class HistoryService:
#     def __init__(self):
#         self.history_repository = HistoryRepository()  # it's better to use dependency injection here
#
#     def get_history_by_user(self, uid: str) -> Optional[History]:
#         return self.history_repository.get_history_by_user(uid)
#
#     def get_history_by_id(self, historyID: int)-> Optional[History]:
#         h: History = self.history_repository.get_history_by_Id(historyID)
#         if h is None:
#             raise NotFoundException('History not found')
#         return h
#
#     def create_history(self, history_data):
#         try:
#             new_history = History(**history_data)
#             success, message = self.history_repository.add_history(new_history)
#             return success, message
#         except Exception as e:
#             raise