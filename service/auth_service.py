from flask_bcrypt import Bcrypt

import datetime

from database.data_handle.user_data_handle import find_user, update_user
from flask_jwt_extended import create_access_token, decode_token


def login(login_info):
    try:
        id = login_info['id']
        password = login_info['password']
    except KeyError:
        return "missingValueError"

    user = find_user(id=id)
    if user is None or type(user) == str:
        return "idIsInvalidError"

    bcrypt = Bcrypt()

    if bcrypt.check_password_hash(user['password'], password=password):
        expires_delta = datetime.timedelta(days=1)
        access_token = create_access_token(identity=id, expires_delta=expires_delta)
        jti = decode_token(access_token)['jti']
        is_success = update_user(id=id, token=jti)

        if type(is_success) == str:
            return "databaseUpdateError"

        return {"token": access_token}
    else:
        return "passwordIsNotMatchedError"


def logout(id):
    is_success = update_user(id=id, token="noToken")

    if type(is_success) == str:
        return "databaseUpdateError"
    else:
        return True


def auth(id, jti):
    user = find_user(id=id)
    if user is None or type(user) == str:
        return "idIsInvalidError"

    if user['token'] == jti:
        return True
    else:
        return "tokenIsInvalidError"
