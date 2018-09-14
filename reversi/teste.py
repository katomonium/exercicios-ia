from flask import Flask, request, app, Response
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/teste": {"origins": "http://localhost:5000"}})


@app.route("/")
# @crossdomain(origin='*')
def hello():
    return "Hello World!"

@app.route("/index")
def oi():
    return "indexx"

@app.route('/teste', methods=['POST'])
# @crossdomain(origin='*')
def foo():
    print("p0")
    json = request.get_json()
    print(json)

    return Response(json)