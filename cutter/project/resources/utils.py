from functools import wraps
from flask import request
from project.resources.user_model import User


def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }, 403
        auth_token = auth_header.split(" ")[1]
        resp = User.decode_auth_token(auth_token)
        if isinstance(resp, str):
            return {
                'status': 'fail',
                'message': resp
            }
        user = User.query.filter_by(id=resp).first()
        if not user or not user.active:
            return {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }, 401
        return f(resp, *args, **kwargs)
    return decorated_function
