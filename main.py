from flask import Flask, render_template, request
from database import user_data
from database import user_data_handle

app = Flask(__name__, template_folder='templates')


@app.route('/')
def main():
    return render_template('map.html')


@app.route('/get')
def get_test():
    data = request.args
    return data['name']


@app.route('/db')
def db():
    result = user_data_handle.find_user_info(id="asdf")
    # user_data.insert_user_info("dfssdfsdgd", "asdf")
    user_data.update_user_info("asdf", changed_store_id=21)

    return str(result)


host = '0.0.0.0'
port = 8000

if __name__ == "__main__":
    app.run(host=host, port=port)
