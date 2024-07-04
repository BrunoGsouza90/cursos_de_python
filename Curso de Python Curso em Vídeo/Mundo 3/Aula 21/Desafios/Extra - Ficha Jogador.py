def ficha(jogador = '<desconhecido>', gols = 0):
    print(f'\033[1:31mO jogador\033[m \033[1:33m{jogador}\033[m \033[1:31mfez\033[m \033[1:33m{gols}\033[m \033[1:31mgols na partida!\033[m')

jogador = str(input('\n\033[1:34mDigite o nome do jogador: \033[m'))
gols = str(input('\033[1:34mDigite a quantidade de gols do jogador: \033[m'))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if len(jogador) > 0:
    ficha(jogador, gols)
else:
    ficha(gols=gols)
input('\n\033[1:34mDigite "sair" para sair: \033[m')