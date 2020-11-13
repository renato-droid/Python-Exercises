n = int(input('Digite um número: '))
tot = 0  # variável tot contará as vezes que ele é divisivel por 1 e ele próprio

for c in range(1, n + 1):  # se em c no intervalo de 1 e o próprio número introduzido

    if n % c == 0:  # se n for divisível por 1 e por ele próprio
        print('\033[1:33m', end=' ')  # apresenta o nº em cor amarela
        tot += 1  # tot conta o nº de vezes que se repete isso
    else:  # senão se
        print('\033[1:31m', end=' ')  # apresenta os nºs não divisíveis em cor vermelha
    print(c, end=' ')  # mostrar os números
print('\n\033[mO número {} foi divísivel {} vezes'.format(n, tot))  # o nº introduzido foi divisível x vezes

if tot == 2:  # se o contador repetir apenas 2 vezes
    print('E por isso ele é PRIMO!')  # então ele é primo
else:  # senão se ele repetir mais ou menos vezes
    print('E por isso ele NÃO É PRIMO!')  # então o número não é primo