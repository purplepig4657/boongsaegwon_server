from flask import Flask, render_template, request, jsonify
from database import user_data, store_data
from database import user_data_handle
import json

app = Flask(__name__, template_folder='templates')


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
    result = user_data_handle.find_user_info(id="asdf")
    # user_data.insert_user_info("gsdgsf", "sgadfsdf")
    user_data.update_user_info("asdf", store_id=21)
    test_json = {
        "name": "asdf",
        "asdf": "asdf"
    }
    store_data.insert_store_info("asdfa", "asdfasd", "asdfasdf", "asdfasdf", menu_info=json.dumps(test_json))
    store_data.update_store_info(store_id=2, name="lsakdjhflksdf")

    return str(result)


host = '0.0.0.0'
port = 8000

if __name__ == "__main__":
    app.run(host=host, port=port)
