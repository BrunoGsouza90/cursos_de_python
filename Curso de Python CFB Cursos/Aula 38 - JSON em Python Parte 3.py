import json

# Dicionários viram Objetos JSON.
dicionario_carros = {
    "Marca":"Honda",
    "Modelo":"HRV",
    "Cor":"Prata"
}

# Listas e Tuplas viram Arrays JSON.
lista_carros = ["Honda","Volkswagem","Ford","Fiat","Chevrolet"]

tupla_carros = ("Honda","Volkswagem","Ford","Fiat","Chevrolet")

json_dicionario_carros = json.dumps(dicionario_carros)
json_lista_carros = json.dumps(lista_carros)
json_tupla_carros = json.dumps(tupla_carros)

print(json_dicionario_carros)
print(json_lista_carros)
print(json_tupla_carros)

json_carros = json.dumps(dicionario_carros, indent=4,separators=(":","="),sort_keys=True)

print(json_carros)
'''
{
    "Nome":"Bruno",
    "Time":"Aviadores",
    "Vivo":"True",
    "Energia":100,
    "Mochila":["Perderneira","Corda","Linha","Arame"],
    "Aeronaves":[
        {"Tipo":"Transporte","Habilidade":80},
        {"Tipo":"Ataque","Habilidade":100},
        {"Tipo":"Reconhecimento","Habilidade":50}
    ]
}
'''

json_jogador = '{"Nome":"Bruno","Time":"Aviadores","Vivo":"True","Energia":100,"Mochila":["Perderneira","Corda","Linha","Arame"],"Aeronaves":[{"Tipo":"Transporte","Habilidade":80},{"Tipo":"Ataque","Habilidade":100},{"Tipo":"Reconhecimento","Habilidade":50}]}'

dicionario_jogador = json.loads(json_jogador)

print(dicionario_jogador)

for c,v in dicionario_jogador.items():
    if c == 'Mochila':
        print('')
        for cont, materiais in enumerate(v):
            print(f'Item {cont + 1} = {materiais}')
    elif c == 'Aeronaves':
        print('')
        for dict in v:
            for chave, valor in dict.items():
                if chave == 'Habilidade':
                    print(f'{chave} = {valor}')