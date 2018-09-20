from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
from app import Reversi
from ia import Arvore

app = Flask(__name__, static_url_path='', static_folder='')
CORS(app)
# @app.route('/play', methods = ['POST'])

# @app.route('/start')
# reversi = Reversi()
@app.route('/start', methods = ['POST'])
def start():
    reversi = Reversi()
    print(jsonify(reversi.getTabuleiro()))
    return jsonify(reversi.getJogo())

@app.route('/move', methods = ['POST'])
def fazerJogada():
    pass

@app.route('/', methods = ['POST'])
def teste():
    return jsonify(reversi.getJogo())

@app.route('/play', methods = ['POST'])
def jogar():
    data = json.loads(request.data)

    pos = data['cell'].split()
    reversi = Reversi(data['tabuleiro'])

    jogadorAtual = 'P'

    jogadaValida = reversi.fazerMovimento(jogadorAtual, (int(pos[0]), int(pos[1]) ))
    jogo = reversi.getJogo()
    jogo['jogadaValida'] = jogadaValida
    return jsonify(jogo)

@app.route('/ia', methods = ['POST'])
def ia():
    data = json.loads(request.data)
    # pos = data['cell'].split()

    reversi = Reversi(data['tabuleiro'])

    jogadorAtual = 'B'

    ia = Arvore(reversi, jogadorAtual)
    jogadaIA = ia.getJogada()
    jogadaValida = reversi.fazerMovimento(jogadorAtual, jogadaIA)
    print(jogadaIA, jogadaValida)
    if not jogadaValida:
        print("DEU RUIM DEMAIS")
        exit(1)
    
    jogo = reversi.getJogo()
    # jogo['jogadaValida'] = jogadaValida
    return jsonify(jogo)
    

app.run(debug=True)


