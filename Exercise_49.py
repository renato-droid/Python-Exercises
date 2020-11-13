n = int(input('Digite um número para ver a sua tabuada: '))  # variável n
for c in range(1,11):  # no c entre o intervalo de 1 a 10
    print('{} x {:2} = {}'.format(n, c, (n * c)))  # a variável n vezes c, dará a sua multiplicação