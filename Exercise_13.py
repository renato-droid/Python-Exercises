s = float(input('Qual é o salário do funcionário?: €'))
s2 = s + (s * 15 / 100)
print('Um funcionário que ganhava {}€, com 15% de aumento, passa a receber €{:.2f}'.format(s,s2))
