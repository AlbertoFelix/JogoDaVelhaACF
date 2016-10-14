'''Jogo da velha criado por Alberto, Clara e Filipe Fernandes'''

'''Imports'''
from termcolor import *
'''Variaveis'''
MatrizJogo = []
Jogador_1  = ''
Jogador_2  = ''
letras = ['A','B','C']
vez = 0
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
            if MatrizJogo[i][j] == '[ X ]':
                print(colored(MatrizJogo[i][j],'blue'), end=' ')
            elif MatrizJogo[i][j] == '[ O ]':
                print(colored(MatrizJogo[i][j],'red'), end=' ')
            else:
                print(MatrizJogo[i][j], end=' ')
        print('\n')

def Decodificador(jogada):
    decodificado = ''
    if jogada[0] == 'A':
        decodificado += '0'
    elif jogada[0] == 'B':
        decodificado += '1'
    elif jogada[0] == 'C':
        decodificado += '2'
    if jogada[1] == '1':
        decodificado += '0'
    elif jogada[1] == '2':
        decodificado += '1'
    elif jogada[1] == '3':
        decodificado += '2'
    return decodificado

def jogar(vez, jogada, MatrizJogo):
    if MatrizJogo[int(jogada[0])][int(jogada[1])] == '[   ]':
        if vez == 0:
            MatrizJogo[int(jogada[0])][int(jogada[1])] = '[ X ]'
        elif vez == 1:
            MatrizJogo[int(jogada[0])][int(jogada[1])] = '[ O ]'
    else:
        print('Você não pode jogar nesse local, pois já tem uma marcação ai!')
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
        print('Muito bem ' + Jogador_1 + ', você ficou com o X, agora aguarde o Jogador 2.')
        Jogador_2 = input('Qual o seu nome Jogador 2? ')
        print('Muito bem ' + Jogador_2 + ', você ficou com o O.\n')
        print('Muito bem ' + Jogador_1 + ' e ' + Jogador_2 + ', estamos prontos para começar!\n')
        printMatriz()
        while True:
            while vez == 0:
                opcao = input('Informe a posição em que você deseja colocar o X, ' + Jogador_1 + ': ')
                opcao = Decodificador(opcao)
                jogar(vez,opcao,MatrizJogo)
                vez = 1
                printMatriz()
            while vez == 1:
                opcao = input('Informe a posição em que você deseja colocar o O, ' + Jogador_2 + ': ')
                opcao = Decodificador(opcao)
                jogar(vez,opcao,MatrizJogo)
                vez = 0
                printMatriz()