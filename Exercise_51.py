print('\033[1:33m==' * 20)
print('\033[1:34m10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('\033[1:33m==' * 20)

a1 = int(input('Primeiro termo: '))  # variável a1 é o primeiro termo
r = int(input('Razão: '))  # variável r é a razão
an = a1 + (10 - 1) * r  # termo geral da progressão aritmética

for c in range(a1, an + r, r):  # em c no intervalo de a1, termo geral mais a razão e a razão
    print('{}'.format(c), end=' -> ')  # mostrar a progressão dos 10 primeiros termos de r em r
print('ACABOU')
