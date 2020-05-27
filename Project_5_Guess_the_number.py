# Projeto 5 - Chute o número (com GUI)
# Objetivo: Criar um algoritmo que gera um valor aleatório e o usuário fica tentando o número até acertar

import random
import PySimpleGUI as sg

class ChuteONumero:
	def __init__(self):
		self.valor_aleatorio = 0
		self.valor_minimo = 1
		self.valor_maximo = 100
		self.tentar_novamente = True

	def Iniciar(self):
		#layout
		layout = [[sg.Text('Seu chute:',size=(20,0))],
		[sg.Input(size=(18,0),key='ValorChute')],
		[sg.Button('Chutar')],
		[sg.Output(size=(30, 10))]]

		#criar uma janela
		self.janela = sg.Window('Chute o numero!', layout)

		self.GerarNumeroAleatorio()
		try:
			#receber os valores
			self.LerValoresDaTela()
			#Fazer algo com esses valores
			while self.tentar_novamente == True:
				if self.evento == 'Chutar':
					self.valor_do_chute = self.valores['ValorChute']
					if int(self.valor_do_chute) > self.valor_aleatorio:
						print('Chute um valor mais baixo!')
						self.LerValoresDaTela()
					elif int(self.valor_do_chute) < self.valor_aleatorio:
						print('Chute um valor mais alto!')
						self.LerValoresDaTela()
					elif int(self.valor_do_chute) == self.valor_aleatorio:
						self.tentar_novamente = False
						print('Parabéns! Você acertou o número !!!')
						self.LerValoresDaTela()
		except:
			print('Favor digitar números entre 1 e 100.')
			self.Iniciar()
	
	def LerValoresDaTela(self):
		self.evento, self.valores = self.janela.Read()


	def GerarNumeroAleatorio(self):
		self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
