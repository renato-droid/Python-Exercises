n = str(input('Digite o seu nome completo: ')).strip() #strip corta os espaços nas frases
nome = n.split() #faz uma lista com os nomes na frase
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {}'.format(nome[0])) #vai encontrar a primeira posição na lista
print('O seu útlimo nome é {}'.format(nome[-1])) #pega na lista, conta o nº de palavras e substrai
#escolhendo sempre a última palavra independente do tamanho