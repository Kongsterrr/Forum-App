from flask import Blueprint

from controllers.history_controller import HistoryController

user_blueprint = Blueprint('history', __name__, url_prefix='/history')

user_blueprint.add_url_rule('/<int:user_id>', view_func=HistoryController.as_view('history'), methods=['GET', 'POST'])
