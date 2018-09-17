from flask import Flask, request, jsonify, send_from_directory
import json

app = Flask(__name__, static_url_path='', static_folder='')

table = []
blacks = []
whites = []

moves = [
    ['0 0'],
    ['1 1', '7 7'],
    ['2 2']
]

@app.route('/')
def root():
    return send_from_directory('', 'index.html')

@app.route('/start', methods = ['POST'])
def start():
    data = json.loads(request.data)
    table = data['table']
    whites = [(3, 3), (4, 4)]
    blacks = [(4, 3), (3, 4)]

    return jsonify({ 'code': 200 })

@app.route('/play', methods = ['POST'])
def add_todo():
    data = json.loads(request.data)
    if(data['cmd'] == 'start'):
        # Star / Restart code here
        print('starting...')
        return jsonify({'code': 200})

    pos = data['cell'].split()

    response = {
        'player': [data['cell']],
        'ai': moves.pop()
    }

    return jsonify(response)


app.run(debug=True)
