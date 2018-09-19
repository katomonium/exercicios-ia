# from flask import Flask, request, jsonify, send_from_directory
# import json

# app = Flask(__name__, static_url_path='', static_folder='')
import copy
class Reversi:


    def __init__(self, tab = None):
        if(tab == None):
            self.tabuleiro = []
            for i in range(8):
                self.tabuleiro.append([])
                for j in range(8):
                    self.tabuleiro[i].append('.')

            self.pecas = {}
            self.pecas['P'] = []
            self.pecas['B'] = []

            self.tabuleiro[4][3] = "P"
            self.tabuleiro[3][4] = "P"
            self.tabuleiro[3][3] = "B"
            self.tabuleiro[4][4] = "B"

            self.pecas['B'] = [(3, 3), (4, 4)]
            self.pecas['P'] = [(4, 3), (3, 4)]
        else:
            self.tabuleiro = tab

            self.pecas = {}
            self.pecas['P'] = []
            self.pecas['B'] = []
            for i in range(len(self.tabuleiro)):
                for j in range(len(self.tabuleiro[i])):
                    if(self.tabuleiro[i][j] == 'P'):
                        self.pecas['P'].append((i,j))
                    if(self.tabuleiro[i][j] == 'B'):
                        self.pecas['B'].append((i,j))

        self.possiveisJogadas = {}
        self.possiveisJogadas['P'] = {}
        self.possiveisJogadas['B'] = {}

        self.inimigo = {}
        self.inimigo['P'] = 'B'
        self.inimigo['B'] = 'P'

        self.atualizaPossiveisJogadas()

    def getTabuleiro(self):
        return self.tabuleiro
    
    def getJogo(self):
        jogo = {}
        jogo['tabuleiro'] = self.tabuleiro
        
        jogadas = {}
        for j in self.possiveisJogadas:
            jogadas[j] = {}
            for key in self.possiveisJogadas[j]:
                stringChave = str(key[0]) + " " + str(key[1])
                jogadas[j][stringChave] = []
                for valor in self.possiveisJogadas[j][key]:
                    stringValor = [valor[0], valor[1]]
                    jogadas[j][stringChave].append(stringValor)
        jogo['possiveisJogadas'] = jogadas

        return jogo


    # @app.route('/')
    # def root(self):
    #     return send_from_directory('', 'index.html')

    # @app.route('/start', methods = ['POST'])
    def start(self):
        # data = json.loads(request.data)
        # table = data['table']


        self.imprimeTabuleiro()

        self.atualizaPossiveisJogadas()

        
        self.modoPvP()


    def modoPvP(self, ):
        jogadorAtual = 'P'
        acabou = False
        while not acabou:
            self.imprimeTabuleiro()
            acabou = self.lerJogada(jogadorAtual)
            jogadorAtual = self.inimigo[jogadorAtual]

    # le a jogada, retorna TRUE se o jogo tiver acabado
    def lerJogada(self, jogadorAtual):
        print('Jogador atual: ' + jogadorAtual)
        print(self.possiveisJogadas[jogadorAtual])
        if(len(self.possiveisJogadas[jogadorAtual]) == 0):
            if(len(self.possiveisJogadas[self.inimigo[jogadorAtual]]) == 0):
                return True
            return False
        i = int(input('Entre com a linha:'))
        j = int(input('Entre com a coluna:'))
        jogada = (i,j)
        if(jogada in self.possiveisJogadas[jogadorAtual]):
            print('Jogada valida')
            self.fazerMovimento(jogadorAtual, jogada)
            return False
        else:
            print('Jogada invalida')
            self.lerJogada(jogadorAtual)
        
    # @app.route('/play', methods = ['POST'])
    # def jogar(self):
    #     data = json.loads(request.data)
    #     if(data['cmd'] == 'start'):
    #         # Star / Restart code here
    #         print('starting...')
    #         # return jsonify({'code': 200})

    #     pos = data['cell'].split()

    #     response = {
    #         'player': [data['cell']],
    #         'ai': moves.pop()
    #     }

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

        # # print(vetorPecas)
        jogadoInimigo = "B"
        if(jogadorAtual == "B"):
            jogadoInimigo = "P"
        
        self.possiveisJogadas[jogadorAtual] = {}

        for peca in vetorPecas:
            # print(peca)
            i = peca[0]
            j = peca[1]

            ############################## arriba ######################################
            iAux = i-1
            acabou = False

            pecasQueSeraoViradas = []
            # print("testando pra cima")
            if(self.tabuleiro[iAux][j] == jogadoInimigo):
                pecasQueSeraoViradas.append((iAux, j))
                iAux -= 1
                while(iAux >= 0 and not acabou):
                    # print("testando posicao: ({}, {})".format(iAux, j))
                    if(self.tabuleiro[iAux][j] == jogadoInimigo):
                        # print("achei")
                        pecasQueSeraoViradas.append((iAux, j))
                    elif(self.tabuleiro[iAux][j] == jogadorAtual):
                        acabou = True
                        pecasQueSeraoViradas = []
                    else:
                        acabou = True
                    iAux -= 1

            if len(pecasQueSeraoViradas) and acabou:
                if (iAux+1, j) in self.possiveisJogadas[jogadorAtual]:
                    for peca in pecasQueSeraoViradas:
                        if(peca not in self.possiveisJogadas[jogadorAtual][(iAux+1, j)]):
                            self.possiveisJogadas[jogadorAtual][(iAux+1, j)].append(peca)
                else:
                    self.possiveisJogadas[jogadorAtual][(iAux+1, j)] = pecasQueSeraoViradas

            ############################## abajo ######################################
            iAux = i+1
            acabou = False
            pecasQueSeraoViradas = []
            # print("testando pra baixo")
            if(self.tabuleiro[iAux][j] == jogadoInimigo):
                pecasQueSeraoViradas.append((iAux, j))
                iAux += 1
                while(iAux < 8 and not acabou):
                    # print("testando posicao: ({}, {})".format(iAux, j))
                    if(self.tabuleiro[iAux][j] == jogadoInimigo):
                        # print("achei")
                        pecasQueSeraoViradas.append((iAux, j))
                    elif(self.tabuleiro[iAux][j] == jogadorAtual):
                        acabou = True
                        pecasQueSeraoViradas = []
                    else:
                        acabou = True

                    iAux += 1

            if len(pecasQueSeraoViradas) and acabou:
                if (iAux-1, j) in self.possiveisJogadas[jogadorAtual]:
                    for peca in pecasQueSeraoViradas:
                        if(peca not in self.possiveisJogadas[jogadorAtual][(iAux-1, j)]):
                            self.possiveisJogadas[jogadorAtual][(iAux-1, j)].append(peca)
                else:
                    self.possiveisJogadas[jogadorAtual][(iAux-1, j)] = pecasQueSeraoViradas

                

            ############################## esquerda ######################################
            jAux = j-1
            acabou = False
            pecasQueSeraoViradas = []
            # print("testando pra esquerda")
            
            if(self.tabuleiro[i][jAux] == jogadoInimigo):
                pecasQueSeraoViradas.append((i, jAux))
                jAux -= 1
                while(jAux >= 0 and not acabou):
                    # print("testando posicao: ({}, {})".format(i, jAux))
                    if(self.tabuleiro[i][jAux] == jogadoInimigo):
                        # print("achei")
                        pecasQueSeraoViradas.append((i, jAux))
                    elif(self.tabuleiro[i][jAux] == jogadorAtual):
                        acabou = True
                        pecasQueSeraoViradas = []
                    else:
                        acabou = True
                    jAux -= 1

            if len(pecasQueSeraoViradas) and acabou:
                if (i, jAux+1) in self.possiveisJogadas[jogadorAtual]:
                    for peca in pecasQueSeraoViradas:
                        if(peca not in self.possiveisJogadas[jogadorAtual][(i, jAux+1)]):
                            self.possiveisJogadas[jogadorAtual][(i, jAux+1)].append(peca)
                else:
                    self.possiveisJogadas[jogadorAtual][(i, jAux+1)] = pecasQueSeraoViradas


            ############################## direita ######################################
            jAux = j+1
            acabou = False
            pecasQueSeraoViradas = []
            # print("testando pra direita")
            if(self.tabuleiro[i][jAux] == jogadoInimigo):
                pecasQueSeraoViradas.append((i, jAux))
                jAux += 1
                while(jAux < 8 and not acabou):
                    # print("testando posicao: ({}, {})".format(i, jAux))
                    if(self.tabuleiro[i][jAux] == jogadoInimigo):
                        # print("achei")
                        pecasQueSeraoViradas.append((i, jAux))
                    elif(self.tabuleiro[i][jAux] == jogadorAtual):
                        acabou = True
                        pecasQueSeraoViradas = []
                    else:
                        acabou = True

                    jAux += 1

            if len(pecasQueSeraoViradas) and acabou:
                if (i, jAux-1) in self.possiveisJogadas[jogadorAtual]:
                    for peca in pecasQueSeraoViradas:
                        if(peca not in self.possiveisJogadas[jogadorAtual][(i, jAux-1)]):
                            self.possiveisJogadas[jogadorAtual][(i, jAux-1)].append(peca)
                else:
                    self.possiveisJogadas[jogadorAtual][(i, jAux-1)] = pecasQueSeraoViradas


            ############################## cima-direita ####################################
            iAux = i-1
            jAux = j+1
            acabou = False
            pecasQueSeraoViradas = []
            # print("testando pra cima-direita")
            if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                pecasQueSeraoViradas.append((iAux, jAux))
                jAux += 1
                iAux -= 1
                while(jAux < 8 and iAux >= 0 and not acabou):
                    # print("testando posicao: ({}, {})".format(iAux, jAux))
                    if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                        # print("achei")
                        pecasQueSeraoViradas.append((iAux, jAux))
                    elif(self.tabuleiro[iAux][jAux] == jogadorAtual):
                        acabou = True
                        pecasQueSeraoViradas = []
                    else:
                        acabou = True

                    jAux += 1
                    iAux -= 1

            if len(pecasQueSeraoViradas) and acabou:
                if (iAux+1, jAux-1) in self.possiveisJogadas[jogadorAtual]:
                    for peca in pecasQueSeraoViradas:
                        if(peca not in self.possiveisJogadas[jogadorAtual][(iAux+1, jAux-1)]):
                            self.possiveisJogadas[jogadorAtual][(iAux+1, jAux-1)].append(peca)
                else:
                    self.possiveisJogadas[jogadorAtual][(iAux+1, jAux-1)] = pecasQueSeraoViradas

                


            ############################## cima-esquerda ######################################
            iAux = i-1
            jAux = j-1
            acabou = False
            pecasQueSeraoViradas = []
            # print("testando pra cima-esquerda")
            if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                pecasQueSeraoViradas.append((iAux, jAux))
                jAux -= 1
                iAux -= 1
                while(jAux >= 0 and iAux >= 0 and not acabou):
                    # print("testando posicao: ({}, {})".format(iAux, jAux))
                    if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                        # print("achei")
                        pecasQueSeraoViradas.append((iAux, jAux))
                    elif(self.tabuleiro[iAux][jAux] == jogadorAtual):
                        acabou = True
                        pecasQueSeraoViradas = []
                    else:
                        acabou = True

                    jAux -= 1
                    iAux -= 1

            if len(pecasQueSeraoViradas) and acabou:
                if (iAux+1, jAux+1) in self.possiveisJogadas[jogadorAtual]:
                    for peca in pecasQueSeraoViradas:
                        if(peca not in self.possiveisJogadas[jogadorAtual][(iAux+1, jAux+1)]):
                            self.possiveisJogadas[jogadorAtual][(iAux+1, jAux+1)].append(peca)
                else:
                    self.possiveisJogadas[jogadorAtual][(iAux+1, jAux+1)] = pecasQueSeraoViradas


            ############################## baixo-direita ######################################
            iAux = i+1
            jAux = j+1
            acabou = False
            pecasQueSeraoViradas = []
            # print("testando pra baixo-direita")
            if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                pecasQueSeraoViradas.append((iAux, jAux))
                jAux += 1
                iAux += 1
                while(jAux < 8 and iAux < 8 and not acabou):
                    # print("testando posicao: ({}, {})".format(iAux, jAux))
                    if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                        # print("achei")
                        pecasQueSeraoViradas.append((iAux, jAux))
                    elif(self.tabuleiro[iAux][jAux] == jogadorAtual):
                        acabou = True
                        pecasQueSeraoViradas = []
                    else:
                        acabou = True

                    jAux += 1
                    iAux += 1

            if len(pecasQueSeraoViradas) and acabou:
                if (iAux-1, jAux-1) in self.possiveisJogadas[jogadorAtual]:
                    for peca in pecasQueSeraoViradas:  
                        if(peca not in self.possiveisJogadas[jogadorAtual][(iAux-1, jAux-1)]):
                            self.possiveisJogadas[jogadorAtual][(iAux-1, jAux-1)].append(peca)
                else:
                    self.possiveisJogadas[jogadorAtual][(iAux-1, jAux-1)] = pecasQueSeraoViradas


            ############################## baixo-esquerda ######################################            
            iAux = i+1
            jAux = j-1
            acabou = False
            pecasQueSeraoViradas = []
            # print("testando pra baixo-esquerda")
            if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                pecasQueSeraoViradas.append((iAux, jAux))
                jAux -= 1
                iAux += 1
                while(jAux >= 0 and iAux < 8 and not acabou):
                    # print("testando posicao: ({}, {})".format(iAux, jAux))
                    if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                        # print("achei")
                        pecasQueSeraoViradas.append((iAux, jAux))
                    elif(self.tabuleiro[iAux][jAux] == jogadorAtual):
                        acabou = True
                        pecasQueSeraoViradas = []
                    else:
                        acabou = True

                    jAux -= 1
                    iAux += 1

            if len(pecasQueSeraoViradas) and acabou:
                if (iAux-1, jAux+1) in self.possiveisJogadas[jogadorAtual]:
                    for peca in pecasQueSeraoViradas:
                        if(peca not in self.possiveisJogadas[jogadorAtual][(iAux-1, jAux+1)]):
                            self.possiveisJogadas[jogadorAtual][(iAux-1, jAux+1)].append(peca)
                else:
                    self.possiveisJogadas[jogadorAtual][(iAux-1, jAux+1)] = pecasQueSeraoViradas



    def imprimeTabuleiro(self):
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
        return s

# def main():
#     r = Reversi()
#     print(r.getJogo())
# main()
