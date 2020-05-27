# Projeto 5 - Chute o número
# Objetivo: Criar um algoritmo que gera um valor aleatório e o usuário fica tentando o número até acertar

import random
import PySimpleGUI as sg

class ChuteONumero:
	def __init__(self):
		self.valor_aleatorio = 0
		self.valor_minimo = 1
		self.valor_maximo = 10
		self.tentar_novamente = True

	def Iniciar(self):
		#layout
		layout = [[sg.text('Seu chute:', size=(20,0))],
		[sg.Input(size=(18,0),key='ValorChute')],
		[sg.Button('Chutar')]
		[sg.Output(size(20,10))],
		]
		#criar uma janela
		self.janela = sg.Window('Chute o numero!')

		self.GerarNumeroAleatorio()
		try:
			while True:
				#receber os valores
				self.evento, self.valores = self.janela.Read()
				self.valor_do_chute = self.valores['ValorChute']
				#Fazer algo com esses valores
				if self.evento == 'Chutar':
					while self.tentar_novamente == True:
						if int(self.valor_do_chute) > self.valor_aleatorio:
							print('Chute um valor mais baixo!')
							self.PedirValorAleatorio()
						elif int(self.valor_do_chute) < self.valor_aleatorio:
							print('Chute um valor mais alto!')
							self.PedirValorAleatorio()
						elif int(self.valor_do_chute) == self.valor_aleatorio:
							self.tentar_novamente = False
							print('Parabéns! Você acertou o número !!!')
			except:
				print('Favor digitar números entre 1 e 100.')
				self.Iniciar()

	def PedirValorAleatorio(self):
		self.valor_do_chute = input('Chute um número: ')

	def GerarNumeroAleatorio(self):
		self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
