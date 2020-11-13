from time import sleep # da biblioteca time importar o sleep, que faz o processo demorar alguns segundos

print('\033[1:36m-=-' * 20) # desenha as linhas em azul marinho
print('\033[1:33mAnalisador de Triângulos') # coloca o analisador de Triângulos
print('\033[1:36m-=-' * 20) # desenha as linhas em azul marinho
sleep(2) # demora 2 segundos para processar

a = float(input('\033[1:30mPrimeiro valor: ')) # indique o valor de a
b = float(input('Segundo valor: ')) # indique o valor de b
c = float(input('Terceiro valor: ')) # indique o valor de c

if a < b + c and b < a + c and c < a + b: # se a for menor que b mais c, e b for menor que a mais c e c for menor que a mais b
    print('Os segmentos acima PODEM FORMAR um triângulo!') # então eles podem formar um triângulo
else: # senão
    print('Os segmentos acima NÃO PODEM formar um triângulo!') # não pode formar um triângulo

