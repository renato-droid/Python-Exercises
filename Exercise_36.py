value = float(input('Valor da casa: €')) # valor da casa
salary = float(input('Salário do comprador: €')) # salário do comprador
age = int(input('Em quantos anos pretendes pagar a casa?: €')) # em quantos anos a casa vai ficar paga

prestacao = value / (age * 12) # a prestação será o nº de anos multiplicado por 12 meses e dividido pelo valor da casa
minimo = salary * 30 / 100 # os 30% do salário do comprador não podem ultrapassar a prestação

print('Para pagar uma casa de {:.2f}€ em {} anos, a prestação será de {:.2f}€'.format(value, age, prestacao)) # declaração

if prestacao <= minimo: # se a prestação for menor ou igual aos 30% do salário do comprador
    print('O empréstimo pode ser CONCEDIDO!') # o empréstimo poderá ser concedido
else: # se não
    print('O empréstimo foi NEGADO!') # o empréstimo não será concedido 
