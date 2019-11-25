from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from settings import API_USER, API_PASSWORD 

class User(object):
    def __init__(self, id, username):
        self.id = id
        self.username = username
    

TEST_USER = User(1, API_USER)


def authenticate(username, password):
    if username == API_USER and safe_str_cmp(
        password.encode('utf-8'),
        API_PASSWORD.encode('utf-8')
    ):
        return TEST_USER


def identity(payload):
    user_id = payload['identity']
    if user_id == TEST_USER.id:
        return TEST_USER


def add_jwt(app):
    return JWT(app, authenticate, identity)
