n = float(input('\033[4;36mQual a velocidade do carro?\033[m ')) #pergunta qual a velociade do carro em float
if n <= 80: #se a velocidade do carro for menor ou igual a 80
    print('\033[1;32mTenha um bom dia! Dirija com segurança.') #conduzacom segurança!
else: #senão
    print('\033[1;31mMULTADO! Você excedeu o limite de velocidade permitido que é de 80 km/h') #vais ser multado
    print('\033[1;31mVocê deve pagar uma multa de {:.2f}€'.format((n-80) * 7)) #o preço a pagar serão 7€ por cada km a mais
    print('\033[1;32mTenha um bom dia, dirija com segurança!') #mas tenha um bom dia e conduza em segurança!
