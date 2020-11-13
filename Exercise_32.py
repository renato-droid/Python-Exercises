from datetime import date # da biblioteca datetime importa date
n = int(input('\033[1:35mQue ano quer analisar? Coloque 0 para analisar o ano atual: ')) # qual é o ano que quer analisar
if n == 0: # se a data for igual a zero
    n = date.today().year # ee irá mostrar a data atual do computador
if 0 == n % 4 and n % 100 != 0 or n % 400 == 0: # se o resto da divisão por 4 for igual a 0 e o resto da divisão por
    # 100 for diferente de 0 ou o resto da divisão por 400 for igual a zero
    print('\033[1:33mO ano {} é BISSEXTO'.format(n)) # o ano será bissexto
else: #senão
    print('\033[1:31mO ano {} NÃO É BISSEXTO'.format(n)) # não será bissexto
