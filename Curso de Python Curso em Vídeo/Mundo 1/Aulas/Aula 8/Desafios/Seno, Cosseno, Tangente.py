from math import sin,cos,tan,radians
angulo = int(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O valor do seno do ângulo {}° é {:.2f}!'.format(angulo,seno))
print('O valor do cosseno do ângulo {}° é {:.2f}!'.format(angulo,cosseno))
print('O valor do tangente do ângulo {}° é {:.2f}!'.format(angulo,tangente))
input('Digite "sair" para sair: ')