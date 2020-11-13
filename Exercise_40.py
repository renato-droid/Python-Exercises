n1 = float(input('Primeira nota: ')) # INSIRA A PRIMEIRA NOTA
n2 = float(input('Segunda nota: ')) # INSIRA A SEGUNDA NOTA

m = (n1 + n2) / 2 # a média entre as duas notas
print('Tirando as notas de {:.1f} no primeiro teste e {:.1f} no segundo teste, a média é de {:.1f}'.format(n1,n2,m))
# coloca a nota do primeiro teste, do segundo teste e a média entre ambos

if m >= 9 and m < 10: # se a média for maior ou igual a 9 e for menor que 10
    print('O aluno está em RECUPERAÇÃO') # o aluno está em RECUPERAÇÃO

elif m >= 10: # senão se a média for maior ou igual a 10
    print('O aluno está APROVADO') # o aluno está APROVADO

elif m < 10: # se a média for menor que 10
    print('O aluno está REPROVADO') # o aluno está REPROVADO