from flask import Flask, request
from flask_cors import CORS
import reversi
import json

app = Flask(__name__)
CORS(app)

REVERSI = reversi.reversi()

@app.route('/start', methods=['POST'])
def start():
    data = json.loads(request.data)
    print(data)

    REVERSI.start2()
    jogadas = {}
    print(REVERSI.possiveisJogadas['P'])
    for k, v in REVERSI.possiveisJogadas['P']:
        print('k: {}   v: {}'.format(k, v))

    print('j: {}'.format(jogadas))
    return json.dumps({ 'jogadas': 200 })

@app.route('/play', methods=['POST'])
def play():
    data = json.loads(request.data)
    print(data)
    x = int(data['cell'][0])
    y = int(data['cell'][2])

    pecas = [(x, y)]


    return json.dumps({ 'player': pecas })

app.run(debug=True)
