n = float(input('\033[1:33mQual é o salário do funcionário? ')) # qual é o salário do funcionário?
up1 = n + (n * 15 / 100) # com 15% de aumento será o salário + 15%
up2 = n + (n * 5 / 100) # com 5 % de aumento será o salário + 5%
if n <= 900: # se o salário for menor ou igual a 900€
    print('\033[34mQuem ganhava {:.2f}€ passará a ganhar {:.2f}€ agora, com um aumento de 15%'.format(n,up1)) # coloca o aumento de 15%
else: #senão
    print('\033[32mQuem ganhava {:.2f}€ passará a ganhar {:.2f}€, com um aumento de 5%'.format(n,up2)) # coloca o aumento de 5%