dicionario = dict()
lista = list()
lista_gols = list()
total_gols = 0
cont = 1
while True:
    print("\n" + "\033[1:31:40m-=\033[m" * 8 + f"\033[1:33:40m {cont}° Pessoa \033[m" + "\033[1:31:40m-=\033[m" * 9)
    nome = str(input(f"\n\033[1:34mDigite o nome do {cont}° Jogador: \033[m"))
    partidas = int(input(f"\n\033[1:34mDigite a quantidade de partidas que o {cont}° Jogador jogou: \033[m"))
    for c in range(partidas):
        gols = int(input(f"\n\033[1:34mDigite a quantidade de gols que o {nome} fez na {c + 1}° Partida: \033[m"))
        lista_gols.append(gols)
        total_gols += gols
    dicionario = {'Nome do Jogador': nome,
                  'N° de Partidas': partidas,
                  'Gols por Partida':lista_gols[:],
                  'Total de Gols': total_gols,
                  }
    lista.append(dicionario)
    lista_gols.clear()
    resposta = str(input("\n\033[1:34mQuer cadastrar outro jogador? \033[m")).strip().upper()[0]
    if resposta not in "SN":
        print("\n\033[1:31:40mOpção Inválida! \033[m")
        resposta = str(input("\n\033[1:34mQuer cadastras outro jogador? \033[m")).strip().upper()[0]
    if resposta == "N":
        break
    total_gols = 0
    cont += 1
print('\033[34m=\033[m' * 50)
print(f'\033[1:31m{'cod.'}\033[m\033[1:35m{'Nome':>10}\033[m\033[1:35m{'Gols':>15}{'Total':>19}\033[m')
print('\033[34m-\033[m' * 50)
for num,jogador in enumerate(lista):
    print(f"\033[1:32m{num:<9}\033[m \033[1:33m{jogador['Nome do Jogador']:<13} {str(jogador['Gols por Partida']):<20}\033[m \033[1:31m{jogador['Total de Gols']}\033[m")
print('\033[34m-\033[m' * 50)
while resposta != 999:
    resposta = int(input(f'\n\033[1:34mDigite o id do jogador...\033[m \033[1:35m"999 para parar"\033[m \033[1:34m:\033[m '))
    if resposta == 999:
        break
    while resposta < 0 or resposta >= len(lista):
        print(f'\n\033[1:31mOpção Inválida!\033[m')
        resposta = int(input(f'\n\033[1:34mDigite o id do jogador que deseja ver as informações:\033[m '))
    for c,k in lista[resposta].items():
        print(f'\n\033[1:33m{c}\033[m \033[1:31m=\033[m \033[1:33m{k}\033[m \033[1:31m!\033[m')
input("\n\033[1:34mDigite \"sair\" para sair: \033[m")