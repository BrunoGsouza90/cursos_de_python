filme = {'Título':'StarWars',
         'Ano':1977,
         'Diretor':'Jorge Lucas',
        }
for c,(k,v) in enumerate(filme.items()):
    print(f'{c} - O {k} é {v}.')

print('')

pessoas = {'Nome':'Gustavo',
           'Sexo':'M',
           'Idade':22
           }
print(pessoas)
print(pessoas['Idade'])
print(f'O {pessoas['Nome']} tem {pessoas['Idade']} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['Peso'] = 98.5
print(pessoas)

print('')

brasil = []
estado1 = {'Uf':'Rio de Janeiro',
          'Sigla':'RJ'
           }
estado2 = {'Uf':'São Paulo',
           'Sigla':'SP'
           }
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['Uf'])
print(brasil[1]['Sigla'])
input('\n\033[1:34mDigite "sair" para sair: \033[m')