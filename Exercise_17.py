from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
c = hypot(oposto,adjacente)
print('O valor da hipotenusa será {:.2f}'.format(c))