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

            self.tabuleiro[4][3] = "B"
            self.tabuleiro[3][4] = "B"
            self.tabuleiro[3][3] = "P"
            self.tabuleiro[4][4] = "P"

            self.pecas['P'] = [(3, 3), (4, 4)]
            self.pecas['B'] = [(4, 3), (3, 4)]
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
            return True
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

            incrementos = [(-1, 0), (1,0), (0,-1), (0,1), (-1, 1), (-1, -1), (1, 1), (1, -1)]

            for incremento in incrementos:
                acabou = False
                iAux = i + incremento[0]
                jAux = j + incremento[1]
                pecasQueSeraoViradas = []

                if(0 <= iAux < 8 and 0 <= jAux < 8 and self.tabuleiro[iAux][jAux] == jogadoInimigo):
                    pecasQueSeraoViradas.append((iAux, jAux))
                    iAux += incremento[0]
                    jAux += incremento[1]
                    while(0 <= iAux < 8 and 0 <= jAux < 8 and not acabou):
                        # print("testando posicao: ({}, {})".format(iAux, j))
                        if(self.tabuleiro[iAux][jAux] == jogadoInimigo):
                            # print("achei")
                            pecasQueSeraoViradas.append((iAux, jAux))
                        elif(self.tabuleiro[iAux][jAux] == jogadorAtual):
                            acabou = True
                            pecasQueSeraoViradas = []
                        else:
                            acabou = True
                        iAux += incremento[0]
                        jAux += incremento[1]

                if len(pecasQueSeraoViradas) and acabou:
                    if (iAux - incremento[0], jAux - incremento[1]) in self.possiveisJogadas[jogadorAtual]:
                        for peca in pecasQueSeraoViradas:
                            if(peca not in self.possiveisJogadas[jogadorAtual][(iAux - incremento[0], jAux - incremento[1])]):
                                self.possiveisJogadas[jogadorAtual][(iAux - incremento[0], jAux - incremento[1])].append(peca)
                    else:
                        self.possiveisJogadas[jogadorAtual][(iAux - incremento[0], jAux - incremento[1])] = pecasQueSeraoViradas



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
