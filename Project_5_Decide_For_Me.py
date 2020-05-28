# Project 5 - Decida por mim
# Objetivo: Faça uma pergunta para o programa e ele terá que te dar uma resposta

import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza!','Não','Sim','Pode ser','Talvez'
        ]
    
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

game = DecidaPorMim()
game.Iniciar()
