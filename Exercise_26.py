n = str(input('Digite uma frase: ')).upper().strip() #n significa o nome
p = n.count('A') # p = posição na frase, conta o nº de A´s na frase
f = n.find('A') + 1 # f = first, primeira posição
l = n.rfind('A') + 1 # l = last, última posição, o rfind conta a partir da direita
print('A letra A aparece {} vezes na frase'.format(p))
print('A primeira letra A apareceu na posição {}'.format(f))
print('A última letra A apareceu na posição {}'.format(l))