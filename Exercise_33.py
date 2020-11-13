n1 = int(input('\033[1:30mPrimeiro valor: '))  # primeiro valor
n2 = int(input('\033[1:33mSegundo valor: '))  # segundo valor
n3 = int(input('\033[1:34mTerceiro valor: '))  # terceiro valor

# Verificando quem é o menor
menor = n1  # o menor número é igual a n1
if n2 < n1 and n2 < n3:  # se o n2 for menor que n1 e menor que n3
    menor = n2  # então o menor número é o n1
if n3 < n1 and n3 < n2:  # se o n3 for menor que n1 e menor que n2
    menor = n3  # então o menor número é o n3

# Verificando quem é o maior
maior = n1  # o maior número é o n1
if n2 > n1 and n2 > n3:  # se o n2 for maior que n1 e que n3
    maior = n2  # então o maior número é o n2
if n3 > n1 and n3 > n2:  # se n3 for maior que n1 e maior que n2
    maior = n3  # então o maior número é o n3
print('\033[1:37mO menor valor digitado foi {}'.format(menor))  # O menor valor digitado será visualizado
print('\033[1:37mO maior valor digitado foi {}'.format(maior))  # o maior número será visualizado
