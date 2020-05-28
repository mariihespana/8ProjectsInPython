# Projeto 7 - Jogo de Aventura (ADAPTADO - MINHA VERSÃO)
# Um jogo de decisões onde terão vários finais diferentes de acordo com cada resposta dada

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

        print(Cenario1)
        self.resposta1 = input(self.pergunta1)
        if self.resposta1 == 'Gregos':
            print(Cenario2)
            self.resposta11 = input(self.pergunta2)

            if self.resposta11 == 'Espada':
                print(Cenario3)
                self.resposta111 = input(self.pergunta3)
                
                if self.resposta111 == 'Cavalaria Pesada do Império':
                    print(self.resultado1)
                if self.resposta111 == 'Guerreiros da Elite':
                    print(self.resultado2)
            
            if self.resposta11 == 'Escudo':
                self.resposta111 = input(self.pergunta3)
                print(Cenario3)
                if self.resposta111 == 'Cavalaria Pesada do Império':
                    print(self.resultado2)
                    exit()
                if self.resposta111 == 'Guerreiros da Elite':
                    print(self.resultado1)
                    exit()
        
        if self.resposta1 == 'Romanos':
            print(Cenario2)
            self.resposta11 = input(self.pergunta2)

            if self.resposta11 == 'Espada':
                print(Cenario3)
                self.resposta111 = input(self.pergunta3)
                
                if self.resposta111 == 'Cavalaria Pesada do Império':
                    print(self.resultado1)
                if self.resposta111 == 'Guerreiros da Elite':
                    print(self.resultado2)
            
            if self.resposta11 == 'Escudo':
                self.resposta111 = input(self.pergunta3)
                print(Cenario3)
                if self.resposta111 == 'Cavalaria Pesada do Império':
                    print(self.resultado2)
                    exit()
                if self.resposta111 == 'Guerreiros da Elite':
                    print(self.resultado1)
                    exit()


Jogo = JogoDeAventura()
Jogo.Iniciar()