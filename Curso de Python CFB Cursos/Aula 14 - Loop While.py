import os
os.system('cls') # Comando utilizado para limpar a tela no terminal.
i = 0
while i < 9:
    print(i)
    i += 1
    if (i >= 5):
        break
print('Fim do looping!')

print('')

i = 0
carros = ["HRV","Golf","Argo","Onix","Focus"]
tamanho = len(carros)
while i < tamanho:
    print(carros[i])
    i += 1
print('Fim do looping!')

print('')

i = 0
carros = []
carro = str(input('Digite o nome do carro: '))
while carro != "-1":
    carros.append(carro)
    carro = str(input('Digite o nome do carro: '))
for x in carros:
    print(x)
print('Fim do looping!')
