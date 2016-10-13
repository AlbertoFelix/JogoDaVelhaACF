'''Jogo da velha criado por Alberto, Clara e Filipe Fernandes'''

'''Imports'''
from termcolor import *
'''Variaveis'''
MatrizJogo = []
Jogador_1  = ''
Jogador_2  = ''
letras = ['A','B','C']
'''Criacao da Matriz do jogo'''
for i in range(3):
	linha = []
	for j in range(3):
		linha.append('[   ]')
	MatrizJogo.append(linha)

'''Funcoes'''
def printMatriz():
    print(colored('   [ 1 ] [ 2 ] [ 3 ]', 'yellow'))
    for i in range(len(MatrizJogo)):
        print(colored('[%s]' % (letras[i]),'yellow'), end='')
        for j in range(len(MatrizJogo[i])):
            print(MatrizJogo[i][j], end= ' ')
        print('\n')

'''Jogo'''
while True:
    print('Seja bem vindo ao Jogo da Velha ACF!\n'
        'Qual modalidade de jogo você deseja jogar?\n'
        'A - Player vs Player\n'
        'B - Player vs IA\n'
        'C - Player vs Player Online\n')
    opcao = input('Qual a sua escolha? ')
    opcao = opcao.upper()
    if opcao == 'A':
        Jogador_1 = input('Qual o seu nome Jogador 1? ')
        print('Muito bem ' + Jogador_1 + ' aguarde agora o Jogador 2.')
        Jogador_2 = input('Qual o seu nome Jogador 2? ')
        print('Muito bem ' + Jogador_1 + ' e ' + Jogador_2 + ', estamos prontos para começar!')
        printMatriz()
        break