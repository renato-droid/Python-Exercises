dias = int(input('Quantos dias foram alugados?: '))
km = float(input('Quantos quilómetros foram percorridos?: '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}€'.format(total))