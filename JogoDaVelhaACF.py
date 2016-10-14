'''Jogo da velha criado por Alberto, Clara e Filipe Fernandes'''

'''Imports'''
from termcolor import *

'''Variaveis'''
Jogador_1  = ''
Jogador_2  = ''
letras = ['A','B','C']
numeros = ['1','2','3']

'''Funcoes'''
def criar_matriz_de_jogo(MatrizJogo):
    for i in range(3):
	    linha = []
	    for j in range(3):
		    linha.append('[   ]')
	    MatrizJogo.append(linha)

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
        return False

def verifica_se_deu_velha(MatrizJogo):
    for i in range(len(MatrizJogo)):
        for j in range(len(MatrizJogo[i])):
            if MatrizJogo[i][j] == '[   ]':
                return False

def verifica_se_o_jogo_acabou(MatrizJogo):
    #Linhas
    if MatrizJogo[0][0] == '[ X ]' and MatrizJogo[0][1] == '[ X ]' and MatrizJogo[0][2] == '[ X ]' or MatrizJogo[0][0] == '[ O ]' and MatrizJogo[0][1] == '[ O ]' and MatrizJogo[0][2] == '[ O ]':
        if MatrizJogo[0][0] == '[ X ]':
            print('Parabéns ' + Jogador_1 + ' você venceu.')
            return True
        elif MatrizJogo[0][0] == '[ O ]':
            print('Parabéns ' + Jogador_2 + ' você venceu.')
            return True
    if MatrizJogo[1][0] == '[ X ]' and MatrizJogo[1][1] == '[ X ]' and MatrizJogo[1][2] == '[ X ]' or MatrizJogo[1][0] == '[ O ]' and MatrizJogo[1][1] == '[ O ]' and MatrizJogo[1][2] == '[ O ]':
        if MatrizJogo[1][0] == '[ X ]':
            print('Parabéns ' + Jogador_1 + ' você venceu.')
            return True
        elif MatrizJogo[1][0] == '[ O ]':
            print('Parabéns ' + Jogador_2 + ' você venceu.')
            return True
    if MatrizJogo[2][0] == '[ X ]' and MatrizJogo[2][1] == '[ X ]' and MatrizJogo[2][2] == '[ X ]' or MatrizJogo[2][0] == '[ O ]' and MatrizJogo[2][1] == '[ O ]' and MatrizJogo[2][2] == '[ O ]':
        if MatrizJogo[2][0] == '[ X ]':
            print('Parabéns ' + Jogador_1 + ' você venceu.')
            return True
        elif MatrizJogo[2][0] == '[ O ]':
            print('Parabéns ' + Jogador_2 + ' você venceu.')
            return True
    #Diagonal Primária
    if MatrizJogo[0][0] == '[ X ]' and MatrizJogo[1][1] == '[ X ]' and MatrizJogo[2][2] == '[ X ]' or MatrizJogo[0][0] == '[ O ]' and MatrizJogo[1][1] == '[ O ]' and MatrizJogo[2][2] == '[ O ]':
        if MatrizJogo[0][0] == '[ X ]':
            print('Parabéns ' + Jogador_1 + ' você venceu.')
            return True
        elif MatrizJogo[0][0] == '[ O ]':
            print('Parabéns ' + Jogador_2 + ' você venceu.')
            return True
    #Diagonal Segundária
    if MatrizJogo[0][2] == '[ X ]' and MatrizJogo[1][1] == '[ X ]' and MatrizJogo[2][0] == '[ X ]' or MatrizJogo[0][2] == '[ O ]' and MatrizJogo[1][1] == '[ O ]' and MatrizJogo[2][0] == '[ O ]':
        if MatrizJogo[0][2] == '[ X ]':
            print('Parabéns ' + Jogador_1 + ' você venceu.')
            return True
        elif MatrizJogo[0][2] == '[ O ]':
            print('Parabéns ' + Jogador_2 + ' você venceu.')
            return True
    #Colunas
    if MatrizJogo[0][0] == '[ X ]' and MatrizJogo[1][0] == '[ X ]' and MatrizJogo[2][0] == '[ X ]' or MatrizJogo[0][0] == '[ O ]' and MatrizJogo[1][0] == '[ O ]' and MatrizJogo[2][0] == '[ O ]':
        if MatrizJogo[0][0] == '[ X ]':
            print('Parabéns ' + Jogador_1 + ' você venceu.')
            return True
        elif MatrizJogo[0][0] == '[ O ]':
            print('Parabéns ' + Jogador_2 + ' você venceu.')
            return True
    if MatrizJogo[0][1] == '[ X ]' and MatrizJogo[1][1] == '[ X ]' and MatrizJogo[2][1] == '[ X ]' or MatrizJogo[0][1] == '[ O ]' and MatrizJogo[1][1] == '[ O ]' and MatrizJogo[2][1] == '[ O ]':
        if MatrizJogo[0][1] == '[ X ]':
            print('Parabéns ' + Jogador_1 + ' você venceu.')
            return True
        elif MatrizJogo[0][1] == '[ O ]':
            print('Parabéns ' + Jogador_2 + ' você venceu.')
            return True
    if MatrizJogo[0][2] == '[ X ]' and MatrizJogo[1][2] == '[ X ]' and MatrizJogo[2][2] == '[ X ]' or MatrizJogo[0][2] == '[ O ]' and MatrizJogo[1][2] == '[ O ]' and MatrizJogo[2][2] == '[ O ]':
        if MatrizJogo[0][2] == '[ X ]':
            print('Parabéns ' + Jogador_1 + ' você venceu.')
            return True
        elif MatrizJogo[0][2] == '[ O ]':
            print('Parabéns ' + Jogador_2 + ' você venceu.')
            return True

'''Jogo'''
while True:
    MatrizJogo = []
    criar_matriz_de_jogo(MatrizJogo)
    vez = 0
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
                if verifica_se_o_jogo_acabou(MatrizJogo) == True:
                    vez = 'Acabou o Jogo.'
                    break
                if verifica_se_deu_velha(MatrizJogo) != False:
                    vez = 'Acabou o Jogo.'
                    print('Deu Velha!')
                    break
                opcao = input('Informe a posição em que você deseja colocar o X(EX: A2), ' + Jogador_1 + ': ')
                opcao = opcao.upper()
                if len(opcao) != 2:
                    print('Você deve ter digitado uma jogada incorreta. Tente Novamente.')
                    break
                if opcao[0] not in letras:
                    print('Você deve colocar uma letra válida!')
                    break
                if opcao[1] not in numeros:
                    print('O número fornecido está incorreto!')
                    break
                opcao = Decodificador(opcao)
                if jogar(vez,opcao,MatrizJogo) == False:
                    break
                vez = 1
                printMatriz()
            while vez == 1:
                if verifica_se_o_jogo_acabou(MatrizJogo) == True:
                    vez = 'Acabou o Jogo.'
                    break
                if verifica_se_deu_velha(MatrizJogo) != False:
                    vez = 'Acabou o Jogo'
                    print('Deu Velha!')
                    break
                opcao = input('Informe a posição em que você deseja colocar o O(EX: B1), ' + Jogador_2 + ': ')
                opcao = opcao.upper()
                if len(opcao) != 2:
                    print('Você deve ter digitado uma jogada incorreta. Tente Novamente.')
                    break
                if opcao[0] not in letras:
                    print('Você deve colocar uma letra válida!')
                    break
                if opcao[1] not in numeros:
                    print('O número fornecido está incorreto!')
                    break
                opcao = Decodificador(opcao)
                if jogar(vez,opcao,MatrizJogo) == False:
                    break
                vez = 0
                printMatriz()
            if vez == 'Acabou o Jogo.':
                jogar_novamente = input('Deseja jogar novamente(sim ou não)? ')
                jogar_novamente = jogar_novamente.lower()
                if jogar_novamente == 'sim':
                    break
                elif jogar_novamente == 'não':
                    print('Volte sempre.')
                    exit()
                else:
                    print('Você não digitou uma opção válida. Digite sim ou não.')
