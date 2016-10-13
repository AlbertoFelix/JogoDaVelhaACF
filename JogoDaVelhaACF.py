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

printMatriz()
