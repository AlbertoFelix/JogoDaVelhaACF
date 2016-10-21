'''Servidor para o jogo da velha ACF'''

'''Imports'''
from socket import *

'''Configuração do Servidor'''
host = '192.168.0.105'
port = 5000
tcp = socket(AF_INET, SOCK_STREAM)
dest = (host, port)

'''Funções'''
def criar_matriz_de_jogo(MatrizJogo):
    for i in range(3):
	    linha = []
	    for j in range(3):
		    linha.append('[   ]')
	    MatrizJogo.append(linha)

def verifica_marcacao_saida (i, j, marcacao_online):
    MatrizJogo[i][j] = marcacao_online

def verifica_marcacao_entrada(i,j):
    if MatrizJogo[i][j] == '[ X ]':
        conexao.send(b'[ X ]')
    elif MatrizJogo[i][j]:
        conexao.send(b'[ O ]')

'''Criando Jogo'''
MatrizJogo = []
criar_matriz_de_jogo(MatrizJogo)
vez = 0
tcp.bind(dest)
tcp.listen(1)

while True:
    conexao, cliente = tcp.accept()

