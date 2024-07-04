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