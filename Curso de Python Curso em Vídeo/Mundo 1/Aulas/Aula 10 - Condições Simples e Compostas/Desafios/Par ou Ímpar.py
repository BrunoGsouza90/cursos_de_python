import math
num = float(input('Digite um número: '))
num = math.trunc(num)
if num % 2 == 0:
    print('O número digitado é par!')
else:
    print('O número digitado é ímpar!')
input('Digite "sair" para sair: ')