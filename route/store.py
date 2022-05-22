from flask import request, jsonify, Blueprint

from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from service import store_service
from service.auth_service import auth


store_route = Blueprint('store_route', __name__, url_prefix='/')


@store_route.route("/get_store_info", methods=['POST'])
def get_store_info():
    store_info = request.get_json()
    result = store_service.get_store_info(store_info=store_info)

    if type(result) == str:
        return jsonify({
            "ok": False,
            "error": result
        })
    else:
        return jsonify({
            "ok": True,
            "error": None,
            "name": result['name'],
            "store_name": result['store_name'],
            "category": result['category'],
            "store_description": result['store_description'],
            "store_open_info": result['store_open_info'],
            "store_photo": result['store_photo'],
            "menu_info": result['menu_info']
        })


@store_route.route("/set_store_info", methods=['POST'])
@jwt_required()
def set_store_info():
    current_user_id = get_jwt_identity()
    if not current_user_id:
        jsonify({
            "ok": False,
            "error": "tokenIsInvalidError"
        })

    jti = get_jwt()['jti']
    if not auth(id=current_user_id, jti=jti):
        return jsonify({
            "ok": False,
            "error": "authenticationFailedError"
        })

    store_info = request.get_json()
    result = store_service.set_store_info(store_info=store_info)

    if type(result) == str:
        return jsonify({
            "ok": False,
            "error": result
        })
    else:
        return jsonify({
            "ok": True,
            "error": None,
        })
