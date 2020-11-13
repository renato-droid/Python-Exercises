s = 0  # o somatório vai começar com 0
count = 0  # o contador vai começar com 0

for n in range(3, 500, 6):  # no n no intevralo entre mútiplos de 3 saltando de 6 em 6 até ao número 500
   if n % 3 == 0:  # se n for divisível por 3 e tiver resto de 0
        count += 1  # o contador vai somar mais um
        s += n  # o somatório vai somar os valores de todos
print('A soma de todos os {} valores solicitados é {}'.format(count, s))

