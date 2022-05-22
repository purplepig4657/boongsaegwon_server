from flask import request, jsonify, Blueprint

from service import register_service


register_route = Blueprint('register_route', __name__, url_prefix='/')


@register_route.route("/register", methods=['POST'])
def register():
    register_info = request.get_json()
    result = register_service.register(register_info=register_info)

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
