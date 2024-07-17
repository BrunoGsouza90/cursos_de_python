estado = {}
brasil = []
for c in range(0,3):
    estado['Uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.keys():
        print(f'O campo {k} tem valor {v}.')
input('\n\033[1:34mDigite "sair" para sair: \033[m')