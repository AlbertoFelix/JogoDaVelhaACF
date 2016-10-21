'''Servidor para o jogo da velha ACF'''

'''Imports'''
from socket import *

'''Configuração do Servidor'''
host = 'localhost'
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
    elif MatrizJogo[i][j] == '[ O ]':
        conexao.send(b'[ O ]')

'''Criando Jogo'''
MatrizJogo = []
criar_matriz_de_jogo(MatrizJogo)
vez = 0
vez_online = 0
Jogador_1 = ''
Jogador_2 = ''
jogada = ''
tcp.bind(dest)
tcp.listen(1)

print('Servidor Iniciado.')
while True:
    conexao, cliente = tcp.accept()
    while True:
        vez_online = bytes(str(vez_online), 'utf-8')
        conexao.send(vez_online)
        transformar = conexao.recv(1024)
        print(transformar[2])
        vez_online = int(transformar[2])
        if vez_online == 0:
            print('Aguardando o nome do Jogador 1.')
            Jogador_1 = conexao.recv(1024)
            conexao.send(Jogador_1)
            vez_online = 1
        elif vez_online == 1:
            print('Aguardando o nome do Jogador 2.')
            Jogador_2 = conexao.recv(1024)
            conexao.send(Jogador_2)

