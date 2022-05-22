from flask import request, jsonify, Blueprint

from flask_jwt_extended import jwt_required, get_jwt_identity
from service import auth_service


login_route = Blueprint('login_route', __name__, url_prefix='/')


@login_route.route("/login", methods=['POST'])
def login():
    login_info = request.get_json()
    result = auth_service.login(login_info=login_info)

    if type(result) == str:
        return jsonify({
            "ok": False,
            "error": result,
            "token": None
        })
    else:
        return jsonify({
            "ok": True,
            "error": None,
            "token": result['token']
        })


@login_route.route("/logout", methods=['POST'])
@jwt_required()
def logout():
    current_user_id = get_jwt_identity()
    if not current_user_id:
        jsonify({
            "ok": False,
            "error": "tokenIsInvalidError"
        })

    result = auth_service.logout(id=current_user_id)

    if type(result) == str:
        jsonify({
            "ok": False,
            "error": result
        })
    else:
        return jsonify({
            "ok": True,
            "error": None
        })


'''
@login_route.route("/auth", methods=['POST'])
@jwt_required()
def auth():
    current_user_id = get_jwt_identity()
    if not current_user_id:
        jsonify({
            "ok": False,
            "error": "tokenIsInvalidError"
        })

    jti = get_jwt()['jti']

    result = auth_service.auth(id=current_user_id, jti=jti)

    return result
'''
