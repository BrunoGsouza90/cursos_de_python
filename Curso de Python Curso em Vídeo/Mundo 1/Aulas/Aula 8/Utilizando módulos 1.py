import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} arredondada para cima é {}!'.format(num,math.ceil(raiz)))
print('A raiz de {} arredondada para baixo é {}!'.format(num,math.floor(raiz)))
from math import pow,ceil
num1 = int(input('Digite outro número por favor:'))
num2 = int(input('Digite o último número por favor:'))
print('A exponenciação de {} é {}!'.format(num1,ceil(pow(num1,num2))))
input('Digite "sair" para sair: ')