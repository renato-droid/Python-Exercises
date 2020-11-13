n = float(input('\033[1:36mQual é a distância da sua viagem? ')) #qual a distância percorrida em azul marinho
if n <= 200: #se a distância for menor ou igual a 200 Km
    print('\033[30mVocê está prestes a iniciar uma viagem de {:.1f}Km'.format(n)) #você está prestes a iniciar uma viagem de X de Km
    print('E o preço da sua passagem será de {:.2f}€'.format(n * 0.50)) #e o preço da passagem será 50 centimos por cada Km
else: #senão
    print('\033[1:31mVocê está prestes a iniciar uma viagem de {:.1f}Km'.format(n)) #você está prestes a iniciar uma viagem de X Km
    print('E o preço da sua passgem será de {:.2f}€'.format(n * 0.45)) #e o preço da passagem será de 45 centimos por cada Km

