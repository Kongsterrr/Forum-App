from functools import wraps

import requests
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
            user_service_url = "http://127.0.0.1:5000/user/" + str('user_id')
            response = requests.get(user_service_url)
            if response.status_code == 200:
                data = response.json()
                token = data.get('token')
                user_status = data.get('user_status')
                return token, user_status
        except:
            raise UnauthorizedException('Token is invalid')

        print(current_user)

        return f(self, current_user, *args, **kwargs)

    return decorator