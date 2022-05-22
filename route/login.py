from flask import Flask, request, jsonify

from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, get_jwt
from service import auth_service


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret_key"
jwt = JWTManager(app)


@app.route("/login", methods=['POST'])
def login():
    login_info = request.get_json()
    result = auth_service.login(login_info=login_info)

    if type(result) == str:
        jsonify({
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


@app.route("/logout", methods=['POST'])
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


@app.route("/auth", methods=['POST'])
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


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
