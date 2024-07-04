def ficha(jogador, gols):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols not in '123456789' or gols == '':
        gols = 0
    print(f'\033[1:31mO Jogador\033[m \033[1:33m{jogador}\033[m \033[1:31mfez\033[m \033[1:33m{gols}\033[m \033[1:31mgol(s) !\033[m')


jogador = str(input('\n\033[1:34mDigite o nome do jogador: \033[m'))
gols = str(input('\n\033[1:34mDigite a quantidade de gols: \033[m'))
ficha(jogador, gols)
input('\n\033[1:34mDigite "sair" para sair: \033[m')