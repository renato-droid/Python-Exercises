from random import randint # da biblioteca random importa randint
from time import sleep # da biblioteca time importa sleep

itens = ('Pedra', 'Papel', 'Tesoura') # variável itens possui pedra, papel e tesoura
desktop = randint(0, 2) # variável desktop vai sortear de 0 a 2

print('''\033[1:30mAs suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
\033[m''') # em branco

player = int(input('Qual é a sua jogada?: '))
print('\033[1:32mJO') # cor verde
sleep(0.5) # espera meio segundo
print('\033[1:34mKEN') # cor azul
sleep(0.5) # espera meio segundo
print('\033[1:35mPO!!') # cor roxa

print('\033[1:31m-=-' * 9) # cor vermelha
print('\033[1:33mComputador jogou {}'.format(itens[desktop])) # amarelo
print('\033[1:33mJogador jogou {}'.format(player)) # amarelo
print('\033[1:31m-=-' * 9) # cor vermelha

if desktop == 0: # se o computador jogar pedra
    if player == 0: # se o player escolher 0
        print('\033[1:33mEMPATE!') # empate, amarelo
    elif player == 1: # senão se escolher 1
        print('\033[1:33mO JOGADOR VENCEU!') # jogador vence, amarelo
    elif player == 2: # senão se escolher 2
        print('\033[1:33mO COMPUTADOR VENCEU!')
    else:
     print('\033[1:36mOpção INVÁLIDA! Tente novamente')

if desktop == 1: # se o computador jogar papel
    if player == 0: # se o player escolher 0
        print('\033[1:33mO COMPUTADOR VENCEU!')
    elif player == 1: # senão se escolher 1
        print('\033[1:33mEMPATE!')
    elif player == 2: # senão se escolher 2
        print('\033[1:33mO JOGADOR VENCEU!')
    else: # senão
     print('\033[1:36mOpção INVÁLIDA! Tente novamente')

if desktop == 2: # se o computador jogar tesoura
    if player == 0: # se o player escolher 0
        print('\033[1:33mO JOGADOR VENCE!')
    elif player == 1: # senão se escolher 1
        print('\033[1:33mO COMPUTADOR VENCEU!')
    elif player == 2: # senão se escolher 2
        print('\033[1:33mEMPATE!')
    else: # senão
     print('\033[1:36mOpção INVÁLIDA! Tente novamente')

