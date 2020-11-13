n =float(input('Digite uma distância em metros: '))
n1 = n / 1000
n2 = n / 100
n3 = n / 10
n4 = n * 10
n5 = n * 100
n6 = n * 1000
print('A medida de {} m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n,n1,n2,n3,n4,n5,n6))