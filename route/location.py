from flask import request, jsonify, Blueprint

from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from service import location_service
from service.auth_service import auth


location_route = Blueprint('location_route', __name__, url_prefix='/')


@location_route.route("/get_location", methods=['POST'])
def get_location_info():
    location_info = request.get_json()
    result = location_service.get_location_info(location_info=location_info)

    if type(result) == str:
        return jsonify({
            "ok": False,
            "error": result
        })
    else:
        return jsonify({
            "ok": True,
            "error": None,
            "store_name": result['store_name'],
            "is_open": result['is_open'],
            "latitude": result['latitude'],
            "longitude": result['longitude']
        })


@location_route.route("/get_all_location", methods=['POST'])
def get_all_location_info():
    result = location_service.get_all_location_info()

    if type(result) == str:
        return jsonify({
            "ok": False,
            "error": result
        })
    else:
        return jsonify({
            "ok": True,
            "error": None,
            "locations": result
        })


@location_route.route("/set_location", methods=['POST'])
@jwt_required()
def set_location_info():
    current_user_id = get_jwt_identity()
    if not current_user_id:
        jsonify({
            "ok": False,
            "error": "tokenIsInvalidError"
        })

    jti = get_jwt()['jti']
    if type(auth(id=current_user_id, jti=jti)) == str:
        return jsonify({
            "ok": False,
            "error": "authenticationFailedError"
        })

    location_info = request.get_json()
    if current_user_id != location_info['id']:
        return jsonify({
            "ok": False,
            "error": "idAndTokenIsNotMatchedError"
        })

    result = location_service.set_location_info(location_info=location_info)

    if type(result) == str:
        return jsonify({
            "ok": False,
            "error": result
        })
    else:
        return jsonify({
            "ok": True,
            "error": None
        })
