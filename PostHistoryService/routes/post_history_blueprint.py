from flask import Blueprint

from controllers.post_history_controller import PostHistoryController

post_history_blueprint = Blueprint('post_history', __name__, url_prefix='/post_history')

post_history_blueprint.add_url_rule('/', view_func=PostHistoryController.as_view('post_history'), methods=['GET'])
