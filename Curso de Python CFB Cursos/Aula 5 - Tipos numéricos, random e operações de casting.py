num_inteiro = 10
num_real = 5.2
num_complexo = 4
num_complexo1 = complex(4,5)

print("Valor: " + str(num_inteiro) + " - Tipo: " + str(type(num_inteiro)))
print("Valor: " + str(num_real) + " - Tipo: " + str(type(num_real)))
print("Valor: " + str(num_complexo) + " - Tipo: " + str(type(num_complexo)))
print("Valor: " + str(num_complexo1) + " - Tipo: " + str(type(num_complexo1)))

x = int(num_real)
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

x = float(num_inteiro)
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

import random

num_inteiro = random.randrange(0,59)
print("Valor: " + str(num_inteiro) + " - Tipo: " + str(type(num_inteiro)))

num_inteiro = [random.randrange(0,59),
random.randrange(0,59),
random.randrange(0,59),
random.randrange(0,59),
random.randrange(0,59),
random.randrange(0,59)
]

print("Valor: " + str(num_inteiro[0]),end=' → ')
print("Valor: " + str(num_inteiro[1]),end=' → ')
print("Valor: " + str(num_inteiro[2]),end=' → ')
print("Valor: " + str(num_inteiro[3]),end=' → ')
print("Valor: " + str(num_inteiro[4]),end=' → ')
print("Valor: " + str(num_inteiro[5]))
nome = 'Bruno'
nome = nome.replace('Lucas')
print(nome)