from flask import Blueprint

from controllers.gateway_controller import *
from utils.utils import get_route


gateway_blueprint = Blueprint('gateway', __name__)

gateway_blueprint.add_url_rule('/<path:path>', view_func=GatewayView.as_view('gateway'), methods=['GET', 'POST', 'PUT'])
gateway_blueprint.before_request(get_route)