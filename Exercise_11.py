l = float(input('Largadura da Parede: '))
a = float(input('Altura da parede: '))
print('A sua parece tem a dimensão de {} x {} e a sua área é de {}m2'.format(l,a,l*a))
print('Para pintar esta parece você irá precisar de {:.2f}l de tinta'.format((l*a)/2))