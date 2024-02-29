from functools import wraps
import config

import jwt
from flask import request

from aop.exceptions import UnauthorizedException


def token_required(f):
    @wraps(f)
    def decorator(self, *args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            raise UnauthorizedException('Token is missing')

        try:
            data = jwt.decode(token[7:], config.JWT_SECURITY_KEY, algorithms=["HS256"])
            user_id = data['user_id']
            # current_user = UserRepository().get_user(data['user_id'])
        except:
            raise UnauthorizedException('Token is invalid')

        return f(self, user_id, *args, **kwargs)

    return decorator
