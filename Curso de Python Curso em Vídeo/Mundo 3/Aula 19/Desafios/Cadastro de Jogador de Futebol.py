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
for num_jogador,jogador in enumerate(lista):
    print("\n " + "\033[1:31:40m-=\033[m" * 6 + f"\033[1:33:40m{num_jogador + 1}° Jogador\033[m" + "\033[1:31:40m-=\033[m" * 6 + "\n")
    for k,v in jogador.items():
        print(f"\033[1:35m{k}\033[m \033[1:31m=\033[m \033[1:33m{v}\033[m")
        if k == 'Gols por Partida':
            print('')
            for num_partida,num_gols in enumerate(v):
                print(f"\033[1:35m==>\033[m\033[1:31m Na\033[m \033[1:33m{num_partida + 1}° Partida\033[m \033[1:31m{jogador['Nome do Jogador']} fez\033[m \033[1:33m{num_gols}\033[m \033[1:31mgols!\033[m")
            print('')
input("\n\033[1:34mDigite \"sair\" para sair: ")