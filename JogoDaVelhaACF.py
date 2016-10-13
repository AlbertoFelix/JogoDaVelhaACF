'''Jogo da velha criado por Alberto, Clara e Filipe Fernandes'''

'''Variaveis'''
MatrizJogo = []

'''Criacao da Matriz do jogo'''
for i in range(3):
	linha = []
	for j in range(3):
		linha.append('[   ]')
	MatrizJogo.append(linha)

'''Funcoes'''
def printMatriz():
	for i in range(len(MatrizJogo)):
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
