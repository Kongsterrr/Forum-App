import datetime
from typing import Optional

import jwt

import config
from aop.exceptions import NotFoundException
from models.history import History
from repos.history_repo import HistoryRepository


class HistoryService:
    def __init__(self):
        self.history_repository = HistoryRepository()  # it's better to use dependency injection here

    def get_history_by_user(self, uid: str) -> Optional[History]:
        return self.history_repository.get_history_by_user(uid)

    def get_history_by_id(self, historyID: int)-> Optional[History]:
        h: History = self.history_repository.get_history_by_Id(historyID)
        if h is None:
            raise NotFoundException('History not found')
        return h

    def create_history(self, history_data):
        try:
            new_history = History(**history_data)
            success, message = self.history_repository.add_history(new_history)
            return success, message
        except Exception as e:
            raise