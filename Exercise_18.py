from math import radians, sin, cos, tan
ang = int(input('Digite o ângulo que tu desejas: '))
seno = sin(radians(ang))
print('O àngulo de {} tem o SENO de {:.1f}'.format(ang,seno))
cosseno = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.1f}'.format(ang,cosseno))
tangente = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.1f}'.format(ang,tangente))
