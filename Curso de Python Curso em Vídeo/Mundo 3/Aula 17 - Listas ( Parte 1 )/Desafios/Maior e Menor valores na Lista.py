#lista = [int(input(f'\n\033[1:34mDigite o {c}° valor: \033[m'))for c in range(1,6)]
#print(f'\033[1:31mA lista é:\033[m \033[1:33m{lista}\033[m \033[1:31m!\033[m')

lista = []
posicao = 1
cont = 1
for c in range(1,6):
    valor = int(input(f'\n\033[1:34mDigite o {c}° valor: \033[m'))
    lista.append(valor)

maior = max(lista)
menor = min(lista)
print(f'\n\033[1:35mO maior número é o\033[m \033[1:33m"{maior}"\033[m \033[1:31me ele(s) esta(ão) na(s) seguint(s) posição(ões): \033[m\n')
for num in lista:
    if num == maior:
        print(f'\033[1:31mO\033[m \033[1:33m{cont}°\033[m \033[1:31mnúmero\033[m \033[1:33m"{maior}"\033[m \033[1:31mestá na\033[m \033[1:33m{posicao}°\033[m \033[1:31mposição!\033[m')
        cont += 1
    posicao += 1
print(f'\n\033[1:31mA lista é:\033[m \033[1:33m{lista}\033[m \033[1:31m!\033[m')
input('\n\033[1:34m''Digite "sair" para sair: \033[m')