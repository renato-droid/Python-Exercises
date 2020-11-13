s = 0  # o somatório começa com 0
count = 0  # o contador começa com 0

for c in range(1,7):  # no c no intervalo de 1 a 6
    n = int(input('Digite o {} valor: '.format(c)))  # ele irá mostrar 6 opções diferentes
    if n % 2 == 0:  # se o n for divisível por 2 e tiver resto de 0
        count += 1  # o contador vai contar o nº de vezes de números pares
        s += n  # o somatório vai somar todos os números pares
print('O somatório dos {} valores pares é {}'.format(count, s))