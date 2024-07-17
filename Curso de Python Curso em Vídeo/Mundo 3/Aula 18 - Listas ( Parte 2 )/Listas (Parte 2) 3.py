galera = list()
dado = list()
maior_idade = list()
total_maior = total_menor = 0
for c in range(1,4):
    dado.append(str(input(f'\nDigite o {c}° nome: ')))
    dado.append(int(input(f'Digite a {c}° idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print(f'Os menores de idade são os: ',end='')
for p in galera:
    if p[1] <= 21:
        maior_idade.append(p[0])
        total_menor += 1
    else:
        total_maior += 1
print(', '.join(maior_idade) + '.')
print(f'\nNo grupo temos {total_maior} maiores de idade e {total_menor} menores de idade!')
