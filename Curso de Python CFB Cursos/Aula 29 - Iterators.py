carros = ['HRV','Polo','Jeta','Cruze','Fusion']
for carro in carros:
    print(carro)

print('')

itCarros = iter(carros)
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))
print(next(itCarros))

print('')

cont = 0
while cont < 5:
    print(carros[cont])
    cont += 1

print('')

itCarros = iter(carros)
while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print('Fim da Lista')
        break