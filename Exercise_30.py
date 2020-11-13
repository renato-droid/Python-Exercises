n = int(input('\033[1:30mMe diga um número qualquer: ')) #diga um nº qauluqer na cor branca
result = n % 2 #o resultado será a divisão do número por 2
if result == 0: #se o resto da divisão for 0
    print('O número {} é PAR!'.format(n)) #então o número é PAR
else: #se não for
    print('O número {} é ÍMPAR!'.format(n)) #então o número é ÍMPAR 
