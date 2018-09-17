# from flask import Flask, request, jsonify, send_from_directory
import json

# app = Flask(__name__, static_url_path='', static_folder='')

tabuleiro = []
pretas = []
brancas = []


# @app.route('/')
def root():
    return send_from_directory('', 'index.html')

# @app.route('/start', methods = ['POST'])
def start():
    # data = json.loads(request.data)
    # table = data['table']
    for i in range(8):
        tabuleiro.append([]);
        for j in range(8):
            tabuleiro[i].append('.')
    tabuleiro[4][3] = "P";
    tabuleiro[3][4] = "P";
    tabuleiro[3][3] = "B";
    tabuleiro[4][4] = "B";

    brancas = [(3, 3), (4, 4)]
    pretas = [(4, 3), (3, 4)]
    printTable()

    calculaPossiveisJogadas("P", pretas)
    tabuleiro[2][3] = "P"
    pretas.append((2, 3))
    viraPecas("P", [(3, 3)], pretas)

    print(pretas)
    printTable()
    # return jsonify({ 'code': 200 })

# @app.route('/play', methods = ['POST'])
def jogar():
    data = json.loads(request.data)
    if(data['cmd'] == 'start'):
        # Star / Restart code here
        print('starting...')
        # return jsonify({'code': 200})

    pos = data['cell'].split()

    response = {
        'player': [data['cell']],
        'ai': moves.pop()
    }

    # return jsonify(response)

def viraPecas(jogadorAtual, vetorPecas, pecasJogador):
    for p in vetorPecas:
        tabuleiro[p[0]][p[1]] = jogadorAtual
        pecasJogador.append(p)

def calculaPossiveisJogadas(jogadorAtual, vetorPecas):
    # print(vetorPecas)
    jogadoInimigo = "B"
    if(jogadorAtual == "B"):
        jogadoInimigo = "P"

    possiveisJogadas = {}
    for peca in vetorPecas:
        print(peca)
        i = peca[0]
        j = peca[1]

        # arriba
        iAux = i-1
        falhou = False

        pecasQueSeraoViradas = []
        print("testando pra cima")
        while(iAux >= 0 and not falhou):
            print("testando posicao: ({}, {})".format(iAux, j))
            if(tabuleiro[iAux][j] == jogadoInimigo):
                print("achei")
                pecasQueSeraoViradas.append((iAux, j))
            else:
                falhou = True
            iAux -= 1

        if len(pecasQueSeraoViradas):
            possiveisJogadas[(iAux+1, j)] = pecasQueSeraoViradas

        # abajo
        iAux = i+1
        falhou = False
        pecasQueSeraoViradas = []
        print("testando pra baixo")
        while(iAux < 8 and not falhou):
            print("testando posicao: ({}, {})".format(iAux, j))
            if(tabuleiro[iAux][j] == jogadoInimigo):
                print("achei")
                pecasQueSeraoViradas.append((iAux, j))
            else:
                falhou = True
            iAux += 1

        if len(pecasQueSeraoViradas):
            possiveisJogadas[(iAux-1, j)] = pecasQueSeraoViradas

        # esquerdja
        jAux = j-1
        falhou = False
        pecasQueSeraoViradas = []
        print("testando pra esquerda")
        while(jAux >= 0 and not falhou):
            print("testando posicao: ({}, {})".format(i, jAux))
            if(tabuleiro[i][jAux] == jogadoInimigo):
                print("achei")
                pecasQueSeraoViradas.append((i, jAux))
            else:
                falhou = True
            jAux -= 1

        if len(pecasQueSeraoViradas):
            possiveisJogadas[(i, jAux+1)] = pecasQueSeraoViradas

        # deretcha
        jAux = j+1
        falhou = False
        pecasQueSeraoViradas = []
        print("testando pra direita")
        while(jAux < 8 and not falhou):
            print("testando posicao: ({}, {})".format(i, jAux))
            if(tabuleiro[i][jAux] == jogadoInimigo):
                print("achei")
                pecasQueSeraoViradas.append((i, jAux))
            else:
                falhou = True
            jAux += 1

        if len(pecasQueSeraoViradas):
            possiveisJogadas[(i, jAux-1)] = pecasQueSeraoViradas

        # cima direita
        iAux = i-1
        jAux = j+1
        falhou = False
        pecasQueSeraoViradas = []
        print("testando pra cima-direita")
        while(jAux < 8 and iAux >= 0 and not falhou):
            print("testando posicao: ({}, {})".format(iAux, jAux))
            if(tabuleiro[iAux][jAux] == jogadoInimigo):
                print("achei")
                pecasQueSeraoViradas.append((iAux, jAux))
            else:
                falhou = True
            jAux += 1
            iAux -= 1

        if len(pecasQueSeraoViradas):
            possiveisJogadas[(iAux+1, jAux-1)] = pecasQueSeraoViradas


        # cima esquerda
        iAux = i-1
        jAux = j-1
        falhou = False
        pecasQueSeraoViradas = []
        print("testando pra cima-esquerda")
        while(jAux >= 0 and iAux >= 0 and not falhou):
            print("testando posicao: ({}, {})".format(iAux, jAux))
            if(tabuleiro[iAux][jAux] == jogadoInimigo):
                print("achei")
                pecasQueSeraoViradas.append((iAux, jAux))
            else:
                falhou = True
            jAux -= 1
            iAux -= 1

        if len(pecasQueSeraoViradas):
            possiveisJogadas[(iAux+1, jAux+1)] = pecasQueSeraoViradas

        # baixo direita
        iAux = i+1
        jAux = j+1
        falhou = False
        pecasQueSeraoViradas = []
        print("testando pra baixo-direita")
        while(jAux < 8 and iAux < 8 and not falhou):
            print("testando posicao: ({}, {})".format(iAux, jAux))
            if(tabuleiro[iAux][jAux] == jogadoInimigo):
                print("achei")
                pecasQueSeraoViradas.append((iAux, jAux))
            else:
                falhou = True
            jAux += 1
            iAux += 1

        if len(pecasQueSeraoViradas):
            possiveisJogadas[(iAux+1, jAux+1)] = pecasQueSeraoViradas


        # baixo esquerda
        iAux = i+1
        jAux = j-1
        falhou = False
        pecasQueSeraoViradas = []
        print("testando pra baixo-esquerda")
        while(jAux >= 0 and iAux < 8 and not falhou):
            print("testando posicao: ({}, {})".format(iAux, jAux))
            if(tabuleiro[iAux][jAux] == jogadoInimigo):
                print("achei")
                pecasQueSeraoViradas.append((iAux, jAux))
            else:
                falhou = True
            jAux -= 1
            iAux += 1

        if len(pecasQueSeraoViradas):
            possiveisJogadas[(iAux-1, jAux+1)] = pecasQueSeraoViradas


        print(possiveisJogadas)
        print("-----------")



def printTable():
    s = '   '
    for i in range(8):
        s += "{} ".format(i)

    s += "\n"

    for i in range(8):
        s += "{}: ".format(i)
        for j in range(8):
            celula = tabuleiro[i][j]
            s += "{} ".format(celula)

        s += '\n'

    print(s)




start()
# app.run(debug=True)
