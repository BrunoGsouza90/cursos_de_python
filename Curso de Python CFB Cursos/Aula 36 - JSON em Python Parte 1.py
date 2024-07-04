import json

json_carros = '{"Marca":"Honda", "Modelo":"HRV", "Cor":"Prata"}'

dicionario_carros = json.loads(json_carros)

print(dicionario_carros)
print(dicionario_carros['Marca'])
print(dicionario_carros['Modelo'])

for x,v in dicionario_carros.items():
    print(f'{x} = {v}')

dicionario_carros = {
                        "Marca":"Honda",
                        "Modelo":"HRV",
                        "Cor":"Prata"
                    }

json_carros = json.dumps(dicionario_carros)

print(json_carros)