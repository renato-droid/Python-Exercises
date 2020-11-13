from datetime import date # da biblioteca datetime importar o metodo date
# atual: variável do ano atual do pc
# idade: variável da idade em anos da pessoa
# n: variável do ano de nascimento
# ano: variável do ano de alistamento 

atual = date.today().year # a variável atual vai dar o ano atual do computador

n = int(input('Ano de nascimento: ')) # ano de nascimento

idade = atual - n # a idade será o ano atual menos o ano em que nasceu
print('Quem nasceu em {}, tem {} anos em {}'.format(n,idade,atual)) # dá a data de nascimento, a idade e o ano atual

if idade < 18: # se a idade for menor que 18
    ano = atual + (18 - idade) # a variável ano será o ano atual mais os anos restantes
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade)) # faltam X anos para o alistamento
    print('O seu alistamento será em {}'.format(ano)) # o alistamento será na data X

elif idade > 18: # senão se idade for maior que 18
    ano = atual - (idade - 18) # a variável ano será o ano atual menos os anos que já passram dos 18
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18)) # os anos que já passaram desde os 18
    print('O seu alistamento deveria ter sido no ano {}'.format(ano)) # o alistamento deveria ter sido no ano X

elif idade == 18: # senão se a idade for igual a 18
    print('Estás na idade do alistamento. Nem te atrevas a faltar!') # tem que se alistar imediatamente