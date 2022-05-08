from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def main():
    return render_template('map.html')


host = '0.0.0.0'
port = 8000

if __name__ == "__main__":
    app.run(host=host, port=port)
