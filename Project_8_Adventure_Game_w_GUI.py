# Projeto 7 - Jogo de Aventura (ADAPTADO - MINHA VERSÃO)
# Um jogo de decisões onde terão vários finais diferentes de acordo com cada resposta dada
# I did a lot of changes and tried to go different from the tutorial when developing this code.

import PySimpleGUI as sg

Cenario0 = 'Você está prestes a iniciar um Jogo de Aventura. Cuidado! Suas escolhas definem o resultado do jogo.'
Cenario1 = 'Você está em uma guerra entre duas nações. As nações são representadas por Gregos e Romanos.'
Cenario2 = 'Infelizmente, não se têm espadas para todos. Durante a luta, você pode escolher entre utilizar um escudo ou uma espada para enfrentar os inimigos.'
Cenario3 = 'Todos os guerreiros podem escolher entre serem treinados por especialistas de guerra.'

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'De qual lado você gostaria de jogar?'
        self.pergunta2 = 'Você escolhe lutar com a espada ou com o escudo?'
        self.pergunta3 = 'Você gostaria de ser treinado pela Cavalaria Pesada do Império ou pelos Guerreiros da Elite?'
        self.resultado1 = 'VOCÊ É UM HERÓI!!! E CONSEGUIU VENCER O OPONENTE!.'
        self.resultado2 = 'VOCÊ NÃO CONSEGUIU VENCER O OPONENTE.'

    def Iniciar(self):

        # layout

        layout =[[sg.Text('Clique em "Seguir o jogo" para Iniciar')],
        [sg.Output(size=(100,10))],
        [sg.Input(size=(30,0),key='escolha')],
        [sg.Button('Seguir o jogo')],
        ]

        # criar a janela
        self.janela = sg.Window('Jogo de Aventura', layout)
        
        self.LerValores()

        print(Cenario1)
        print(self.pergunta1)
        self.LerValores()
        
        while True:

            if self.valores['escolha'] == 'Gregos':
                print(Cenario2)
                print(self.pergunta2)
                self.LerValores()

                if self.valores['escolha'] == 'Espada':
                    print(Cenario3)
                    print(self.pergunta3)
                    self.LerValores()
                    
                    if self.valores['escolha'] == 'Cavalaria Pesada do Império':
                        print(self.resultado1)
                        self.LerValores()                            
                        exit()
                    if self.valores['escolha'] == 'Guerreiros da Elite':
                        print(self.resultado2)
                        self.LerValores()
                        exit()

                if self.valores['escolha'] == 'Escudo':
                    print(self.pergunta3)
                    print(Cenario3)
                    self.LerValores()

                    if self.valores['escolha'] == 'Cavalaria Pesada do Império':
                        print(self.resultado2)
                        self.LerValores()

                    if self.valores['escolha'] == 'Guerreiros da Elite':
                        print(self.resultado1)
                        self.LerValores()
            
            if self.valores['escolha'] == 'Romanos':
                print(Cenario2)
                print(self.pergunta2)
                self.LerValores()

                if self.valores['escolha'] == 'Espada':
                    print(Cenario3)
                    print(self.pergunta3)
                    self.LerValores()
                    
                    if self.valores['escolha'] == 'Cavalaria Pesada do Império':
                        print(self.resultado1)
                        self.LerValores()
                    if self.valores['escolha'] == 'Guerreiros da Elite':
                        print(self.resultado2)
                        self.LerValores()
                
                if self.valores['escolha'] == 'Escudo':
                    print(Cenario3)
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'Cavalaria Pesada do Império':
                        print(self.resultado2)
                        self.LerValores()
                    if self.valores['escolha'] == 'Guerreiros da Elite':
                        print(self.resultado1)
                        self.LerValores()
        
    def LerValores(self):
        # ler os valores da tela
        self.evento, self.valores = self.janela.Read()

Jogo = JogoDeAventura()
Jogo.Iniciar()
