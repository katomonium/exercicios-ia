# from flask import Flask, request, jsonify, send_from_directory
import json

# app = Flask(__name__, static_url_path='', static_folder='')
class reversi:


    def __init__(self):
        self.tabuleiro = []

        self.pecas = {}
        self.pecas['P'] = []
        self.pecas['B'] = []

        self.possiveisJogadas = {}
        self.possiveisJogadas['P'] = {}
        self.possiveisJogadas['B'] = {}

        self.inimigo = {}
        self.inimigo['P'] = 'B'
        self.inimigo['B'] = 'P'


    # @app.route('/')
    def root(self):
        return send_from_directory('', 'index.html')

    # @app.route('/start', methods = ['POST'])
    def start(self):
        # data = json.loads(request.data)
        # table = data['table']
        for i in range(8):
            self.tabuleiro.append([])
            for j in range(8):
                self.tabuleiro[i].append('.')
        self.tabuleiro[4][3] = "P"
        self.tabuleiro[3][4] = "P"
        self.tabuleiro[3][3] = "B"
        self.tabuleiro[4][4] = "B"

        self.pecas['B'] = [(3, 3), (4, 4)]
        self.pecas['P'] = [(4, 3), (3, 4)]
        self.imprimeTabela()

        self.calculaPossiveisJogadas("P")

        self.fazerMovimento('P', (2,3))
        # print(self.pecas['P'])

        self.fazerMovimento('B', (2,2))
        self.imprimeTabela()

        self.fazerMovimento('P', (3,2))
        self.imprimeTabela()
        # return jsonify({ 'code': 200 })

    # @app.route('/play', methods = ['POST'])
    def jogar(self):
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

    def fazerMovimento(self, jogadorAtual, posicao):
        if posicao in self.possiveisJogadas[jogadorAtual]:
            inimigo = self.inimigo[jogadorAtual]
            self.tabuleiro[posicao[0]][posicao[1]] = jogadorAtual
            self.pecas[jogadorAtual].append(posicao)
            pecasASeremViradas = self.possiveisJogadas[jogadorAtual][posicao]
            for p in pecasASeremViradas:
                self.tabuleiro[p[0]][p[1]] = jogadorAtual
                self.pecas[jogadorAtual].append(p)
                self.pecas[inimigo].remove(p)
            self.atualizaPossiveisJogadas()
        else:
            return False

    def atualizaPossiveisJogadas(self):
        self.calculaPossiveisJogadas('P')
        self.calculaPossiveisJogadas('B')

    def calculaPossiveisJogadas(self, jogadorAtual):

        vetorPecas = self.pecas[jogadorAtual]

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
                if(self.tabuleiro[iAux][j] == jogadoInimigo):
                    print("achei")
                    pecasQueSeraoViradas.append((iAux, j))
                else:
                    falhou = True
                iAux -= 1

            if len(pecasQueSeraoViradas):
                self.possiveisJogadas[jogadorAtual][(iAux+1, j)] = pecasQueSeraoViradas

            # abajo
            iAux = i+1
            falhou = False
            pecasQueSeraoViradas = []
            print("testando pra baixo")
            while(iAux < 8 and not falhou):
                print("testando posicao: ({}, {})".format(iAux, j))
                if(self.tabuleiro[iAux][j] == jogadoInimigo):
                    print("achei")
                    pecasQueSeraoViradas.append((iAux, j))
                else:
                    falhou = True
                iAux += 1

            if len(pecasQueSeraoViradas):
                self.possiveisJogadas[jogadorAtual][(iAux-1, j)] = pecasQueSeraoViradas

            # esquerdja
            jAux = j-1
            falhou = False
            pecasQueSeraoViradas = []
            print("testando pra esquerda")
            while(jAux >= 0 and not falhou):
                print("testando posicao: ({}, {})".format(i, jAux))
                if(self.tabuleiro[i][jAux] == jogadoInimigo):
                    print("achei")
                    pecasQueSeraoViradas.append((i, jAux))
                else:
                    falhou = True
                jAux -= 1

            if len(pecasQueSeraoViradas):
                self.possiveisJogadas[jogadorAtual][(i, jAux+1)] = pecasQueSeraoViradas

            # deretcha
            jAux = j+1
            falhou = False
            pecasQueSeraoViradas = []
            print("testando pra direita")
            while(jAux < 8 and not falhou):
                print("testando posicao: ({}, {})".format(i, jAux))
                if(self.tabuleiro[i][jAux] == jogadoInimigo):
                    print("achei")
                    pecasQueSeraoViradas.append((i, jAux))
                else:
                    falhou = True
                jAux += 1

            if len(pecasQueSeraoViradas):
                self.possiveisJogadas[jogadorAtual][(i, jAux-1)] = pecasQueSeraoViradas

            # cima direita
            iAux = i-1
            jAux = j+1
            falhou = False
            pecasQueSeraoViradas = []
            print("testando pra cima-direita")
            while(jAux < 8 and iAux >= 0 and not falhou):
                print("testando posicao: ({}, {})".format(iAux, jAux))
                if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                    print("achei")
                    pecasQueSeraoViradas.append((iAux, jAux))
                else:
                    falhou = True
                jAux += 1
                iAux -= 1

            if len(pecasQueSeraoViradas):
                self.possiveisJogadas[jogadorAtual][(iAux+1, jAux-1)] = pecasQueSeraoViradas


            # cima esquerda
            iAux = i-1
            jAux = j-1
            falhou = False
            pecasQueSeraoViradas = []
            print("testando pra cima-esquerda")
            while(jAux >= 0 and iAux >= 0 and not falhou):
                print("testando posicao: ({}, {})".format(iAux, jAux))
                if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                    print("achei")
                    pecasQueSeraoViradas.append((iAux, jAux))
                else:
                    falhou = True
                jAux -= 1
                iAux -= 1

            if len(pecasQueSeraoViradas):
                self.possiveisJogadas[jogadorAtual][(iAux+1, jAux+1)] = pecasQueSeraoViradas

            # baixo direita
            iAux = i+1
            jAux = j+1
            falhou = False
            pecasQueSeraoViradas = []
            print("testando pra baixo-direita")
            while(jAux < 8 and iAux < 8 and not falhou):
                print("testando posicao: ({}, {})".format(iAux, jAux))
                if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                    print("achei")
                    pecasQueSeraoViradas.append((iAux, jAux))
                else:
                    falhou = True
                jAux += 1
                iAux += 1

            if len(pecasQueSeraoViradas):
                self.possiveisJogadas[jogadorAtual][(iAux+1, jAux+1)] = pecasQueSeraoViradas


            # baixo esquerda
            iAux = i+1
            jAux = j-1
            falhou = False
            pecasQueSeraoViradas = []
            print("testando pra baixo-esquerda")
            while(jAux >= 0 and iAux < 8 and not falhou):
                print("testando posicao: ({}, {})".format(iAux, jAux))
                if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                    print("achei")
                    pecasQueSeraoViradas.append((iAux, jAux))
                else:
                    falhou = True
                jAux -= 1
                iAux += 1

            if len(pecasQueSeraoViradas):
                self.possiveisJogadas[jogadorAtual][(iAux-1, jAux+1)] = pecasQueSeraoViradas


            print(possiveisJogadas)
            print("-----------")



    def imprimeTabela(self):
        s = '   '
        for i in range(8):
            s += "{} ".format(i)

        s += "\n"

        for i in range(8):
            s += "{}: ".format(i)
            for j in range(8):
                celula = self.tabuleiro[i][j]
                s += "{} ".format(celula)

            s += '\n'

        print(s)
        print(self.pecas)


def main():
    r = reversi()
    r.start()


main()
# app.run(debug=True)
