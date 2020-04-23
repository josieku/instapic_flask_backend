from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth
from app.main.service.user_service import get_a_user


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')
        current_user = None

        if not token:
            response_object = {
                'status': 'fail',
                'message': 'token required'
            }
            return response_object, 401
        else:
            user_id = token.get('user_id')
            current_user = get_a_user(user_id)

        return f(*args, **kwargs, current_user=current_user)

    return decorated