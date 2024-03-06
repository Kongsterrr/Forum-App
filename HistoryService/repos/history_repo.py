from typing import Optional

from aop.exceptions import NotFoundException
from models.history import History
from models.database import db

class HistoryRepository:
    def get_history_by_Id(self, historyId) -> Optional[History]:
        return db.query(History).get(historyId)

    def get_history_by_user(self, userId) -> Optional[History]:
        return db.query(History).filter(
            History.userId == userId
        ).all()
    def add_history(self, new_history):
        db.add(new_history)
        try:
            db.commit()
            return True, "History recorded successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)

    def delete_history(self, historyId):
        db.delete(History)
        try:
            db.commit()
            return True, "History deleted successfully."
        except Exception as e:
            db.rollback()
            return False, str(e)