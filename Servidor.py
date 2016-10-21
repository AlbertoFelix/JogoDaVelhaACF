'''Servidor para o jogo da velha ACF'''

'''Imports'''
from socket import *

'''Configuração do Servidor'''
host = '192.168.0.105'
port = 5000
tcp = socket(AF_INET, SOCK_STREAM)
dest = (host, port)

