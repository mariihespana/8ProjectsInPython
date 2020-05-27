# Projeto 3 - Chute o número
# Objetivo: Criar um algoritmo que gera um valor aleatório e o usuário fica tentando o número até acertar

import random

class ChuteONumero:
	def __init__(self):
		self.valor_aleatorio = 0
		self.valor_minimo = 1
		self.valor_maximo = 10
		self.tentar_novamente = True

	def Iniciar(self):
		self.GerarNumeroAleatorio()
		self.PedirValorAleatorio()
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


	def PedirValorAleatorio(self):
		self.valor_do_chute = input('Chute um número: ')

	def GerarNumeroAleatorio(self):
		self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
