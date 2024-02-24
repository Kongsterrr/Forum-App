from functools import wraps
import config

from repos.user_repo import UserRepository
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
            current_user = UserRepository().get_user_by_Id(data['user_id'])
        except:
            raise UnauthorizedException('Token is invalid')

        print(current_user)

        return f(self, current_user, *args, **kwargs)

    return decorator
