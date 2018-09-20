from app import Reversi
from copy import deepcopy

def inverteCor(cor):
    if(cor == "P"):
        return "B"
    else:
        return "P"

class Arvore:
    def __init__(self, reversi, cor = 'B'):
        self.maiorSaldo = None
        self.melhorJogada = None
        self.filhos = []
        self.cor = cor
        self.calculaFilhos(reversi)

    def calculaFilhos(self, reversi):
        for jogada in reversi.possiveisJogadas[self.cor]:
            re = deepcopy(reversi)
            re.fazerMovimento(self.cor, jogada)
            nohFilho = Noh(re, self.cor, 0, 3, jogada, self)
            self.filhos.append(nohFilho)
    
    def getJogada(self):
        return self.melhorJogada
    

class Noh:
    def __init__(self, reversi, cor, nivel, nivelMax, jogadaInicial, arvore):
        self.reversi = reversi
        self.cor = cor
        self.nivel = nivel
        self.nivelMax = nivelMax
        self.jogadaInicial = jogadaInicial
        self.arvore = arvore
        self.filhos = []

        ehFolha = nivel < nivelMax
        acabou = False
        if(nivel % 2 == 0):
            corOponente = inverteCor(self.cor)
            if not len(self.reversi.possiveisJogadas[corOponente]):
                ehFolha = True
        else:
            if not len(self.reversi.possiveisJogadas[self.cor]):
                ehFolha = True


        if not ehFolha:
            if(oponente):
                self.jogadaOponente()
            else:
                self.jogadaIA()
        else:
            saldo = len(self.reversi.pecas[self.cor])
            if(self.arvore.maiorSaldo == None):
                self.arvore.maiorSaldo = saldo
                self.arvore.melhorJogada = self.jogadaInicial
            else:
                if(saldo > self.arvore.maiorSaldo):
                    self.arvore.maiorSaldo = saldo
                    self.arvore.melhorJogada = self.jogadaInicial

            
    def jogadaOponente(self):
        corOponente = inverteCor(self.cor)
        melhorJogadaOponente = None
        qntPecasMelhorJogada = 0
        for jogada in self.reversi.possiveisJogadas[corOponente]:
            qntPecasViradas = len(self.reversi.possiveisJogadas[corOponente][jogada]) 
            if(qntPecasViradas > qntPecasMelhorJogada):
                qntPecasMelhorJogada = qntPecasViradas
                melhorJogadaOponente = jogada
            # elif(qntPecasViradas == qntPecasMelhorJogada):
                # fazer um random maneiro aqui

        re = deepcopy(self.reversi)
        re.fazerMovimento(corOponente, melhorJogadaOponente)

        nohFilho = Noh(re, self.cor, self.nivel+1, self.nivelMax, self.jogadaInicial, self.arvore)
        self.filhos.append(nohFilho)
    
    def jogadaIA(self):
        for jogada in self.reversi.possiveisJogadas[self.cor]:
            re = deepcopy(self.reversi)
            re.fazerMovimento(self.cor, jogada)
            nohFilho = Noh(re, self.cor, self.nivel+1, 3, self.jogadaInicial, self.arvore)
            self.filhos.append(nohFilho)

def main():
    re = Reversi()
    ia = Arvore(re)

    print(ia.melhorJogada)
    


main()
    




