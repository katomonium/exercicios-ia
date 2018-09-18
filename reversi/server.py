from flask import Flask, request, jsonify, send_from_directory
import json
from app import Reversi

app = Flask(__name__, static_url_path='', static_folder='')

# @app.route('/play', methods = ['POST'])

# @app.route('/start')
@app.route('/start', methods = ['POST'])
def root():
    reversi = Reversi()
    print(jsonify(reversi.getTabuleiro()))
    return jsonify(reversi.getJogo())
    # return send_from_directory('', 'index.html')

app.run(debug=True)

