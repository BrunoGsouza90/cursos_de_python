carro = {
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
}

print(carro['Modelo'])
fabricante = carro['Fabricante']
fabricante = carro.get('Fabricante')
print(fabricante)

print('')

carro['Cor'] = 'Preto'
carro['Cambio'] = 'Automático'
print(carro)
print(carro['Cor'])
print('')
for x in carro:
    print(x,end=' = ')
    print(carro[x])
print('')
for k,v in carro.items():
    print(f'{k} = {v}')
print('')
for v in carro.values():
    print(v)
print('')
for k in carro.keys():
    print(k)

print('')

if 'Modelo' in carro:
    print('Sim, modelo é uma chave!')

print('')

print(f'Tamanho do Dicionário: {len(carro)}')
carro.pop('Cambio')
print(carro)
del carro['Cor']
print(carro)
print('')
carro.clear()
print(carro)

print('')

carro = {
    'Carro1':{
        'Fabricante':'Honda',
        'Modelo':'HRV',
        'Cor':'Preto'
    },
    'Carro2':{
        'Fabricante':'Volkswagem',
        'Modelo':'Golf',
        'Cor':'Vermelho'
    },
    'Carro3':{
        'Fabricante':'Ford',
        'Modelo':'Focus',
        'Cor':'Branco'
    }
}

print(carro['Carro1'])
print(carro['Carro1']['Fabricante'])

print('')

for c in carro.values():
    for x,c in c.items():
        print(f'{x} = {c}')

print('')


Carro1 = {
    'Fabricante':'Honda',
    'Modelo':'HRV',
    'Cor':'Preto'
}
Carro2 = {
    'Fabricante':'Volkswagem',
    'Modelo':'Golf',
    'Cor':'Vermelho'
}
Carro3 = {
    'Fabricante':'Ford',
    'Modelo':'Focus',
    'Cor':'Branco'
}

carro = {
    'C1': Carro1,
    'C2': Carro2,
    'C3': Carro3,
}
print(carro['C1'])
print(carro['C1']['Modelo'])