from flask import Blueprint

from controllers.history_controller import *

history_blueprint = Blueprint('history', __name__, url_prefix='/history')

history_blueprint.add_url_rule('/', view_func=HistoryCreateController.as_view('history_create'), methods=['POST'])
history_blueprint.add_url_rule('/<int:uid>', view_func=HistoryController.as_view('history'), methods=['GET'])
