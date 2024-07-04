import math
oposto=float(input('\nDigite o comprimento do cateto oposto: '))
adjacente=float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('A hipotenusa dos catetos descritos é \033[31m{:.2f}\033[m!'.format(hipotenusa))
input('\n\033[1:34mDigite sair para sair: \033[m')
