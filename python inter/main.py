#Importa as bibliotecas necessárias
from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
import random
from functools import partial
from random import randint

from PyQt5.QtWidgets import QPushButton


class menu():
    #Inicia as variaveis globais dos jogos
    def __init__(self):
        #variaveis forca
        self.correta, self.dica = self.palavra()
        self.vida = 7
        self.letras_chutadas = []
        self.kamudo = []
        self.primeira = True
        self.letraMudada = self.correta
        #Variavel Jogo da velha
        self.turno = 0
        #variavel jo ken po
        self.pcEscolha = 0
        self.userpoints = 0
        self.pcpoints = 0
        self.empatespoints = 0
        #Inicia as telas dos jogos
        app = QtWidgets.QApplication([])
        self.menu = uic.loadUi('telas/menu.ui')
        self.forca = uic.loadUi('telas/Jogoforca.ui')
        self.velha = uic.loadUi('telas/Jogovelha.ui')
        self.sair = uic.loadUi('telas/sair.ui')
        self.joken = uic.loadUi('telas/joken.ui')
        self.memomoria = uic.loadUi('telas/jogomemoria.ui')
        #Abre as telas ao clicar nos botoes
        self.menu.botaosair.clicked.connect(self.sairTela)
        self.menu.botaoforca.clicked.connect(self.abrirForca)
        self.menu.botaovelha.clicked.connect(self.abrirVelha)
        self.menu.botaojoken.clicked.connect(self.abrirJoken)
        self.menu.botaomemo.clicked.connect(self.abrirmemo)
        #Abre o menu e excuta o programa
        self.menu.show()
        app.exec()
    #Abre a tela sair e fecha tudo
    def sairTela(self):
        self.menu.close()
        self.sair.show()
    #Sai do JokenPo e abre o menu
    def sairJokenPo(self):
        self.joken.close()
        self.menu.show()

    def abrirmemo(self):
        self.menu.close()
        self.memomoria.sairmemo.clicked.connect(self.sairmemo)
        self.b1 = self.memomoria.findChild(QPushButton, "b1")
        self.b2 = self.memomoria.findChild(QPushButton, "b2")
        self.b3 = self.memomoria.findChild(QPushButton, "b3")
        self.b4 = self.memomoria.findChild(QPushButton, "b4")
        self.b5 = self.memomoria.findChild(QPushButton, "b5")
        self.b6 = self.memomoria.findChild(QPushButton, "b6")
        self.b7 = self.memomoria.findChild(QPushButton, "b7")
        self.b8 = self.memomoria.findChild(QPushButton, "b8")
        self.b9 = self.memomoria.findChild(QPushButton, "b9")
        self.b10 = self.memomoria.findChild(QPushButton, "b10")
        self.b11 = self.memomoria.findChild(QPushButton, "b11")
        self.b12 = self.memomoria.findChild(QPushButton, "b12")
        self.b13 = self.memomoria.findChild(QPushButton, "b13")
        self.b14 = self.memomoria.findChild(QPushButton, "b14")
        self.b15 = self.memomoria.findChild(QPushButton, "b15")
        self.b16 = self.memomoria.findChild(QPushButton, "b16")

        self.b1.clicked.connect(self.click)
        self.b2.clicked.connect(self.click)
        self.b3.clicked.connect(self.click)
        self.b4.clicked.connect(self.click)
        self.b5.clicked.connect(self.click)
        self.b6.clicked.connect(self.click)
        self.b7.clicked.connect(self.click)
        self.b8.clicked.connect(self.click)
        self.b9.clicked.connect(self.click)
        self.b10.clicked.connect(self.click)
        self.b11.clicked.connect(self.click)
        self.b12.clicked.connect(self.click)
        self.b13.clicked.connect(self.click)
        self.b14.clicked.connect(self.click)
        self.b15.clicked.connect(self.click)
        self.b16.clicked.connect(self.click)



        self.memomoria.show()


    def sairmemo(self):
        self.memomoria.close()
        self.menu.show()

    #Abre e inicia o Jo ken po
    def abrirJoken(self):
        #Fecha o menu
        self.menu.close()
        #Roda o jogo quando o user apertar algum botao
        self.joken.pedra.clicked.connect(self.stone)
        self.joken.tesoura.clicked.connect(self.cut)
        self.joken.papel.clicked.connect(self.paper)
        #Inicaliza os pontos
        self.joken.pcp.setText("0")
        self.joken.userp.setText("0")
        self.joken.emp.setText("0")
        #Sai do jogo
        self.joken.sairjoken.clicked.connect(self.sairJokenPo)
        #Mostra a tela do Jo Ken Po
        self.joken.show()
    #Abre e inicia a forca
    def abrirForca(self):
        #Deixa as imagens escondidas
        self.forca.chute.setHidden(True)
        self.forca.cabeca.setHidden(True)
        self.forca.corpo.setHidden(True)
        self.forca.besquerdo.setHidden(True)
        self.forca.bdireito.setHidden(True)
        self.forca.pesquerdo.setHidden(True)
        self.forca.pdireito.setHidden(True)
        self.forca.luffy.setHidden(True)
        #Chama a função das vidas
        self.prints(self)
        #Começa a forca
        self.forca.enviar2.clicked.connect(self.jogoForca)
        #Sai da forca
        self.forca.sairforca.clicked.connect(self.sairForca)
        #Destroi o menu
        self.menu.destroy()
        #Mostra a tela forca
        self.forca.show()

    # Abre e inicia o jogo da velha
    def abrirVelha(self):
        #Incializa os botoes
        botoes = [self.velha.bt1, self.velha.bt2, self.velha.bt3, self.velha.bt4,self.velha.bt5,self.velha.bt6,self.velha.bt7,self.velha.bt8,self.velha.bt9]
        for j in botoes:
            j.clicked.connect(partial(self.jogoVelha, j))
        #Sai da velha
        self.velha.sairvelha.clicked.connect(self.sairVelha)
        #Destroi o menu
        self.menu.destroy()
        #mostra a tela do jogo da velha
        self.velha.show()
    #Sai da forca
    def sairForca(self):
        self.forca.destroy()

    #Sai do jogo da velha
    def sairVelha(self):
        self.velha.destroy()


    #Jogo da velha
    def jogoVelha(self, bt):
        #Configura os botoes
        botoes = [self.velha.bt1, self.velha.bt2, self.velha.bt3, self.velha.bt4, self.velha.bt5, self.velha.bt6,
                  self.velha.bt7, self.velha.bt8, self.velha.bt9]
        #Checa a vez e coloca faz o jogo funcionar
        if self.turno % 2 == 0:
            if bt.text() == "":
                self.velha.vez.setText("Vez do X")
                bt.setText("O")
                bt.setEnabled(False)
        else:
            if bt.text() == "":
                self.velha.vez.setText("Vez do O")
                bt.setText("X")
                bt.setEnabled(False)
        #checa se alguem venceu ou deu velha
        if self.Xvencedor():
            self.velha.vez.setText("X venceu, O noob")
            for j in botoes:
                j.setEnabled(False)

        elif self.Ovencedor():
            self.velha.vez.setText("O venceu, X pato")
            for j in botoes:
                j.setEnabled(False)

        if self.turno >= 8:
            self.velha.vez.setText("Deu velha, ambos ruins")

        self.turno += 1



    #Checagem caso o X vença
    def Xvencedor(self):
        #Init dos botoes
        botoes = [
            [self.velha.bt1, self.velha.bt2, self.velha.bt3],
            [self.velha.bt4, self.velha.bt5, self.velha.bt6],
            [self.velha.bt7, self.velha.bt8, self.velha.bt9]
        ]

        if botoes[0][0].text() == "X" and botoes[0][1].text() == "X" and botoes[0][2].text() == "X":
            return True
        elif botoes[1][0].text() == "X" and botoes[1][1].text() == "X" and botoes[1][2].text() == "X":
            return True
        elif botoes[2][0].text() == "X" and botoes[2][1].text() == "X" and botoes[2][2].text() == "X":
            return True
        elif botoes[0][0].text() == "X" and botoes[1][0].text() == "X" and botoes[2][0].text() == "X":
            return True
        elif botoes[0][1].text() == "X" and botoes[1][1].text() == "X" and botoes[2][1].text() == "X":
            return True
        elif botoes[0][2].text() == "X" and botoes[1][2].text() == "X" and botoes[2][2].text() == "X":
            return True
        elif botoes[0][0].text() == "X" and botoes[1][1].text() == "X" and botoes[2][2].text() == "X":
            return True
        elif botoes[0][2].text() == "X" and botoes[1][1].text() == "X" and botoes[2][0].text() == "X":
            return True
    #Checagem caso o O vença
    def Ovencedor(self):
        # Init dos botoes
        botoes = [
            [self.velha.bt1, self.velha.bt2, self.velha.bt3],
            [self.velha.bt4, self.velha.bt5, self.velha.bt6],
            [self.velha.bt7, self.velha.bt8, self.velha.bt9]
        ]

        if botoes[0][0].text() == "O" and botoes[0][1].text() == "O" and botoes[0][2].text() == "O":
            return True
        elif botoes[1][0].text() == "O" and botoes[1][1].text() == "O" and botoes[1][2].text() == "O":
            return True
        elif botoes[2][0].text() == "O" and botoes[2][1].text() == "O" and botoes[2][2].text() == "O":
            return True

        elif botoes[0][0].text() == "O" and botoes[1][0].text() == "O" and botoes[2][0].text() == "O":
            return True
        elif botoes[0][1].text() == "O" and botoes[1][1].text() == "O" and botoes[2][1].text() == "O":
            return True
        elif botoes[0][2].text() == "O" and botoes[1][2].text() == "O" and botoes[2][2].text() == "O":
            return True

        elif botoes[0][0].text() == "O" and botoes[1][1].text() == "O" and botoes[2][2].text() == "O":
            return True
        elif botoes[0][2].text() == "O" and botoes[1][1].text() == "O" and botoes[2][0].text() == "O":
            return True

    #Jogo da forca
    def jogoForca(self):
        #Sai da forca
        self.forca.sairforca.clicked.connect(self.sairForca)
        #inicializa o jogo
        if self.primeira:
            self.forca.chute.setHidden(False)
            self.forca.enviar2.setText("Enviar")
            self.forca.Informacoes.setText("Dica: " + self.dica + "\nTamanho: " + str(len(self.correta)) + " letras")
            self.primeira = False
            for i in range(len(self.correta)):
                self.kamudo.append("_ ")
            self.forca.palavracerta.setText("".join(self.kamudo))
        else:
            #Pega a letra do user e checa ela
            self.forca.palavracerta.setText("".join(self.kamudo))
            letra = self.forca.chute.text()

            self.forca.chute.setText("")
            situacao = self.verificar(letra)
            #Perde uma vida caso o user erre a letra
            if not situacao:
                self.vida -= 1
            self.prints(self.vida)
    #Verificação se a letra chutada está correta
    def verificar(self, letrachutada):
        count = 0
        self.letras_chutadas.append(letrachutada)
        #Checa se a letra está correta
        for i in self.correta:
            if letrachutada == i:
                for x in range(len(self.correta)):
                    if self.correta[x] == letrachutada:
                        self.kamudo[x] = letrachutada

                self.letraMudada = self.letraMudada.replace(letrachutada, "")
                count -= 1
                break
            else:
                count += 1

        self.forca.letraschutadas.setText(" ".join(self.letras_chutadas))

        if count == len(self.correta):
            return False

        elif len(self.letraMudada) == 0:
            self.forca.palavracerta.setText("Você ganhou\n a palavra era: " + self.correta)
            self.forca.Informacoes.setText("")
            self.forca.chute.setEnabled(False)
            return True

        else:
            self.forca.palavracerta.setText("".join(self.kamudo))
            self.forca.letraschutadas.setText(" ".join(self.letras_chutadas))
            return True
    #Escolha da palavra aletoriamente
    def palavra(self):
        dicas = ["jogo", "enigma", "Instrutor mais brabo", "Instrutor mais monstro", "o mais gostoso da ets",
                  "coringa", "Presidente", "Extinto", "KA KA KA"]
        pla = ["forca", "charada", "clebinho", "leonardo", "wilson", "palhaço", "vargas",
               "dinossauro", "kamudo"]
        plac = random.choice(pla)
        palacorreta = plac
        dicain = pla.index(palacorreta)
        dica = dicas[dicain]
        return palacorreta, dica
    #Mostra a vida/personagem caso o user erre
    def prints(self, vida):
        if vida == 6:
            self.forca.cabeca.setHidden(False)
        if vida == 5:
            self.forca.corpo.setHidden(False)
        if vida == 4:
            self.forca.besquerdo.setHidden(False)
        if vida == 3:
            self.forca.bdireito.setHidden(False)
        if vida == 2:
            self.forca.pesquerdo.setHidden(False)
        if vida == 1:
            self.forca.pdireito.setHidden(False)
        if vida == 0:
            self.forca.luffy.setHidden(False)
            self.forca.palavracerta.setText("Você perdeu\n"
                                            "A palavra era: \n" + self.correta)
            self.forca.chute.setEnabled(False)
            self.forca.Informacoes.setText("")


    #Jogo Jo ken Po
    #Caso o jogador escolha pedra
    def stone(self):
        self.joken.user.setText("Pedra")
        choice = self.pcChoice()
        if choice == 0:
            self.joken.pc.setText("Pedra")
            self.joken.winner.setText("Empate")
            self.empatespoints += 1
            self.joken.emp.setText(str(self.empatespoints))
        elif choice == 2:
            self.joken.pc.setText("Tesoura")
            self.joken.winner.setText("Usuário Ganhou")
            self.userpoints += 1
            self.joken.userp.setText(str(self.userpoints))
        elif choice == 1:
            self.joken.pc.setText("Papel")
            self.joken.winner.setText(str("Computador Ganhou"))
            self.pcpoints += 1
            self.joken.pcp.setText(str(self.pcpoints))



    # Caso o jogador escolha tesoura
    def cut(self):
        self.joken.user.setText("Tesoura")
        choice = self.pcChoice()
        if choice == 2:
            self.joken.pc.setText("Tesoura")
            self.joken.winner.setText("Empate")
            self.empatespoints += 1
            self.joken.emp.setText(str(self.empatespoints))
        elif choice == 1:
            self.joken.pc.setText("Papel")
            self.joken.winner.setText("Usuário Ganhou")
            self.userpoints += 1
            self.joken.userp.setText(str(self.userpoints))
        elif choice == 0:
            self.joken.pc.setText("Pedra")
            self.joken.winner.setText("Computador Ganhou")
            self.pcpoints += 1
            self.joken.pcp.setText(str(self.pcpoints))

    # Caso o jogador escolha papel
    def paper(self):
        self.joken.user.setText("Papel")
        choice = self.pcChoice()
        if choice == 1:
            self.joken.pc.setText("Papel")
            self.joken.winner.setText("Empate")
            self.empatespoints += 1
            self.joken.emp.setText(str(self.empatespoints))
        elif choice == 0:
            self.joken.pc.setText("Pedra")
            self.joken.winner.setText("Usuário Ganhou")
            self.userpoints += 1
            self.joken.userp.setText(str(self.userpoints))
        elif choice == 2:
            self.joken.pc.setText("Tesoura")
            self.joken.winner.setText("Computador Ganhou")
            self.pcpoints += 1
            self.joken.pcp.setText(str(self.pcpoints))

    #Escolha do computador
    def pcChoice(self):
        self.pcEscolha = random.randint(0, 2)
        return self.pcEscolha


    #Jogo da memória
    def jogoMemoria(self):
        self.cards = [self.memomoria.b1,
                 self.memomoria.b2,
                 self.memomoria.b3,
                 self.memomoria.b4,
                 self.memomoria.b5,
                 self.memomoria.b6,
                 self.memomoria.b7,
                 self.memomoria.b8,
                 self.memomoria.b9,
                 self.memomoria.b10,
                 self.memomoria.b11,
                 self.memomoria.b12,
                 self.memomoria.b13,
                 self.memomoria.b14,
                 self.memomoria.b15,
                 self.memomoria.b16]
        self.imgs = ["img/luffy.jpg",
                "img/luffy.jpg",
                "img/zoro.jpg",
                "img/zoro.jpg",
                "img/sanji.png",
                "img/sanji.png",
                "img/nami.png",
                "img/nami.png",
                "img/usopp.png",
                "img/usopp.png",
                "img/nami robin.png",
                "img/nami robin.png",
                "img/chopper.png",
                "img/chopper.png",
                "img/franky.jpg",
                "img/franky.jpg"]
        random.shuffle(self.imgs)

    def click(self):
        self.count += 1
        if self.count % 2 != 0:
            b = self.sender()
            for btoes in self.cards:
                if btoes == b:
                    ind = self.cards.index(btoes)
                    btoes.setIcon(QtGui.QIcon(str(self.imgs[ind])))
        else:
            b2 = self.sender()
            for btoes in self.cards:
                if btoes == b2:
                    ind = self.cards.index(btoes)
                    btoes.setIcon(QtGui.QIcon(str(self.imgs[ind])))







if __name__ == '__main__':
    c = menu()
