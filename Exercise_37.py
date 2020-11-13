from time import sleep # da biblioteca time importar o comando sleep

n = int(input('Digite um número inteiro: ')) # digite o número inteiro

print('''\033[1:33mEscolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL\033[m''') # com cor amarela apresentaas 3 opções

sleep(1) # espera 2 segundos

player = int(input('A sua opção: ')) # indique a sua opção

if player == 1: # se for escolhido a opção 1
    print('\033[1:35m{} convertido para BINÁRIO é {}'.format(n,bin(n)[2:])) # o nº é convertido em binário

elif player == 2: # senão se for escolhido a opção 2
    print('\033[1:35m{} convertido para OCTAL é {}'.format(n,oct(n)[2:])) # o nº é convertido em octal

elif player == 3: #senão se for escolhido a opção 3
    print('\033[1:35m{} convertido para HEXADECIMAL é {}'.format(n,hex(n)[2:])) # o nº é convertido para hexadecimal

else:
    print('\033[1:31mOpção inválida. Tente novamente!') # se não for colocada nenhuma das 3 opções, foi inválido
