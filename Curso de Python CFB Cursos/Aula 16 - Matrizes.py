carros = ["HRV","Golf","Focus","Argo"]
for x in carros:
    print(x)                                # Chamado de Array / List.
print(carros[1])
carros[2] = "Fusion"

print('')

carros = [
    ["Modelo","HRV"],
    ["Fabricante","Honda"],
    ["Ano",2016]
]
carros.append(["Cor","Prata"])
print(carros[1][1])
print(carros[2][0])
carros[2][1] = 2019
print('')
for l,c in carros:
    print("Linha: " + l + " | Coluna: " , str(c))
print('')
