from flask import Flask, render_template, request, jsonify

from database.data_operation import store_data, user_data
from database.data_handle import store_data_handle, user_data_handle, location_data_handle
from flask_jwt_extended import JWTManager

from route import login, store

import json

app = Flask(__name__, template_folder='templates')

app.config["JWT_SECRET_KEY"] = "secret_key"
jwt = JWTManager(app)


app.register_blueprint(login.login_route)
app.register_blueprint(store.store_route)


@app.route('/')
def main():
    return render_template('map.html')


@app.route('/get')
def get_test():
    data = request.args
    return data['name']


@app.route('/post', methods=['POST'])
def post_test():
    data = request.form['name']
    return data


@app.route('/json', methods=['POST'])
def json_test():
    data = jsonify(request.json)
    return data


@app.route('/db')
def db():
    user_data_handle.create_user(id="asdfasdf", password="asdf")
    test_open_info = {
        "information": [
            "월, 화 -> 대전광역시 유성구 ~ 16시 ~ 20시",
            "월, 화 -> 대전광역시 유성구 ~ 12시 ~ 20시",
        ]
    }
    test_photo_info = {
        "photo_urls": [
            "photo_url",
            "photo_url",
        ]
    }
    test_menu_info = {
        "menu": [
            { "name": "음식", "price": 10000, "photo": "photo_url", },
            { "name": "음식", "price": 20000, "photo": "photo_url", },
        ]
    }

    store_data_handle.update_store(store_id=2, store_name="asdfasdf", store_open_info=json.dumps(test_open_info),
                                   store_photo=json.dumps(test_photo_info), menu_info=json.dumps(test_menu_info))
    result = user_data_handle.find_user(id="asdf")
    user_data_handle.update_user(id="d", password="sdkfjksdjf", store_id=243)
    print(store_data_handle.find_store(store_id=2))
    # user_data.insert_user_info("gsdgsf", "sgadfsdf")
    user_data.update_user_info("asdf", store_id=21)
    test_json = {
        "name": "asdf",
        "asdf": "asdf"
    }
    # store_data_handle.update_store(store_id=2, store_name="asdfasdf", menu_info=json.dumps(test_json))
    location_data_handle.update_location(store_id=2, latitude=24.24523, longitude=53.42432)
    # store_data.insert_store_info("asdfa", "asdfasd", "asdfasdf", "asdfasdf", menu_info=json.dumps(test_json))
    store_data.update_store_info(store_id=2, name="lsakdjhflksdf")

    return str(result)


host = '0.0.0.0'
port = 8000

if __name__ == "__main__":
    app.run(host=host, port=port)
