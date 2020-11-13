from random import randint  # importa o randint da pasta random
from time import sleep  # da bibliioteca time ele importa o sleep

desktop = randint(0, 10)  # Faz o computador sortear um dos nºs entre 0 a 10
print('\033[1:33m-=-' * 20)  # desenha 20 linhas destas
print('\033[1:34mVou pensar em um número de 0 a 10. Tente adivinhar...\033[m')  # coloca a frase
print('\033[1:33m-=-' * 20)  # desenha 20 linhas destas

player = int(input('Digite um número: '))  # a variável player pede para digitar um número
print('PROCESSANDO...')  # Está a processar
sleep(3)  # sleep é uma ferramenta que faz o comando esperar determinados segundos

if desktop == player:  # se o desktop for igual a player
    print('VENCES-TE! Conseguiste adivinhar em que número eu estava a pensar!')  # ele coloca isto
else:  # senão
    print('VENCI! Eu pensei no número {} e não no {} que colocaste!'.format(desktop, player))  # ele colpca isto
