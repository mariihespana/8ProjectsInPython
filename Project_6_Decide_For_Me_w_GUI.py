# Project 6 - Decida por mim com GUI
# Objetivo: Faça uma pergunta para o programa e ele terá que te dar uma resposta

import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza!','Não','Sim','Pode ser','Talvez'
        ]
    
    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Escreva abaixo uma pergunta ao sistema.')],
            [sg.Input(size=(50,0))],
            [sg.Button('Decida por mim!')],
            [sg.Output(size=(40,0))]
        ]

        # criar uma janela
        self.janela = sg.Window('Game', layout)
        
        while True:

        # ler os valores da tela
            self.evento, self.valores = self.janela.Read()

            if self.evento == "Decida por mim!":
                print(random.choice(self.respostas))

game = DecidaPorMim()
game.Iniciar()
