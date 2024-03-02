from functools import wraps
import config

import jwt
from flask import request

from aop.exceptions import UnauthorizedException, InvalidTokenError

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise UnauthorizedException("Authorization token is missing")

        token_parts = token.split()
        if len(token_parts) == 2:    # "Bearer <token>" from Postman
            token = token_parts[1]
        elif len(token_parts) == 1:
            token = token_parts[0]

        try:
            payload = jwt.decode(token, config.JWT_SECURITY_KEY, algorithms=['HS256'])
            # Add user_id and user_status to kwargs for easy access in route functions
            kwargs['user_id'] = payload.get('user_id')
            kwargs['user_status'] = payload.get('user_status')
            if not kwargs['user_id'] or not kwargs['user_status']:
                raise InvalidTokenError("Invalid token")
        except jwt.ExpiredSignatureError:
            raise InvalidTokenError("Token has expired")
        except jwt.InvalidTokenError:
            raise InvalidTokenError("Invalid token")

        return f(*args, **kwargs)

    return decorated_function


# def token_required(f):
#     @wraps(f)
#     def decorator(self, *args, **kwargs):
#         token = None
#         if 'Authorization' in request.headers:
#             token = request.headers['Authorization']
#
#         if not token:
#             raise UnauthorizedException('Token is missing')
#
#         try:
#             data = jwt.decode(token[7:], config.JWT_SECURITY_KEY, algorithms=["HS256"])
#             current_user = UserRepository().get_user_by_Id(data['user_id'])
#         except:
#             raise UnauthorizedException('Token is invalid')
#
#         print(current_user)
#
#         return f(self, current_user, *args, **kwargs)
#
#     return decorator


