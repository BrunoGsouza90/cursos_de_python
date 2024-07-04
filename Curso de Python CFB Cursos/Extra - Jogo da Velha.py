import emoji,random,time

lista = list()

print(f'\n    \033[1:40m {emoji.emojize("\u274C \U0001f534",language= "pt")} Bem - Vindo ao Jogo da Velha {emoji.emojize("\u274C \U0001f534",language= "pt")}\033[m')
print('\n\033[1:32:40m1\033[m\033[1:33:40m - Para dar velha digite "999".             \033[m')
print('\033[1:32:40m2\033[m\033[1:33:40m - Caso não haja mais opções de jogada digite "0".\033[m')
def matrix_nula():
    cont = 1
    for c in range(0,3):
        lista.append([])
        for i in range(0,3):
            lista[c].append(cont)
            cont += 1
    print('')
    for c in lista:
        print(' ' * 12,end='')
        for i in range(0,3):
            print(f'\033[1:33m[\033[m\033[1:35m{c[i]:^15}\033[m\033[1:33m]\033[m', end=' ')
        print('')

def quem_e_quem():
    quem_comeca = random.randint(1, 2)
    if quem_comeca == 1:
        print('\n\033[4:34mVocê começa Jogador 1\033[m')
        jogador1 = str(input('\n\033[1:34mDigite qual você quer ser Jogador 1:\033[m \033[1:33m[\033[m\033[1:35mX\033[m\033[1:33m]\033[m \033[1:31m/\033[m \033[1:33m[\033[1:35mO\033[m\033[1:33m]\033[m ')).strip().upper()[0]
        while jogador1 not in "XO":
            print("\n\033[1:31:40mOpção Inválida!\033[m")
            jogador1 = str(input('\n\033[1:34mDigite qual você quer ser:\033[m \033[1:33m[\033[m\033[1:35mX\033[m\033[1:33m]\033[m\033[1:31m/\033[m\033[1:33m[\033[m\033[1:35mO\033[m\033[1:33m]\033[m ')).strip().upper()[0]
        if jogador1 == 'X':
            print(f'\n\033[1:34mVocê escolheu o\033[m \033[1:35m{emoji.emojize('\u274C',language='pt')}\033[m \033[1:33mJogador 1\033[m\033[1:34m!\033[m')
            print(f'\033[1:33mJogador 2\033[m \033[1:34mvocê é o {emoji.emojize('\U0001f534',language='pt')} !\033[m')
            jogador2 = "O"
        if jogador1 == 'O':
            print(f'\n\033[1:34mVocê escolheu o\033[m \033[1:35m{emoji.emojize('\U0001f534',language='pt')}\033[m \033[1:33mJogador 1\033[m\033[1:34m!\033[m')
            print(f'\033[1:33mJogador 2\033[m \033[1:34mvocê é o {emoji.emojize('\u274C', language='pt')} !\033[m')
            jogador2 = 'X'
    else:
        print('\n\033[4:34mVocê começa Jogador 2\033[m')
        jogador2 = str(input('\n\033[1:34mDigite qual você quer ser:\033[m \033[1:33m[\033[m\033[1:35mX\033[m\033[1:33m]\033[m\033[1:31m/\033[m\033[1:33m[\033[m\033[1:35mO\033[m\033[1:33m]\033[m ')).strip().upper()[0]
        while jogador2 not in "XO":
            print("\n\033[1:31:40mOpção Inválida!\033[m")
            jogador2 = str(input('\n\033[1:34mDigite qual você quer ser Jogador 2:\033[m \033[1:33m[\033[m\033[1:35mX\033[m\033[1:33m]\033[m\033[1:31m/\033[m\033[1:33m[\033[m\033[1:35mO\033[m\033[1:33m]\033[m ')).strip().upper()[0]
        if jogador2 == 'X':
            print(f'\n\033[1:34mVocê escolheu o\033[m \033[1:35m{emoji.emojize('\u274C',language='pt')}\033[m \033[1:33mJogador 2\033[m\033[1:34m!\033[m')
            print(f'\033[1:33mJogador 1\033[m \033[1:34mvocê é o {emoji.emojize('\U0001f534', language='pt')} !\033[m')
            jogador1 = 'O'
        if jogador2 == 'O':
            print(f'\n\033[1:34mVocê escolheu o\033[m \033[1:35m{emoji.emojize('\U0001f534',language='pt')}\033[m \033[1:33mJogador 2\033[m\033[1:34m!\033[m')
            print(f'\033[1:33mJogador 1\033[m \033[1:34mvocê é o {emoji.emojize('\u274C', language='pt')} !\033[m')
            jogador1 = 'X'
        return(jogador1)
        return(jogador2)

def jogando():
    quem_comeca = random.randint(1,2)
    X = 0
    O = 0
    if quem_comeca == 1:
        print(f'\n\033[1:34mVocê começa {emoji.emojize('\u274C', language='pt')} !\033[m\n')
    elif quem_comeca == 2:
        print(f'\n\033[1:34mVocê começa {emoji.emojize('\U0001f534', language='pt')} !\033[m\n')


    while True:
        for c in lista:
            print(' ' * 12, end='')
            for i in range(0,3):
                print(f'\033[1:33m[\033[m\033[1:35m{str(c[i]):^15}\033[m\033[1:33m]\033[m', end=' ')
            print('')
        if quem_comeca == 1:
            X = int(input(f'\n\033[1:34mDigite a posição\033[m \033[1:33m{emoji.emojize('\u274C',language= 'pt')}\033[m\033[1:34m: \033[m'))
            if X == 999:
                print(f'\n\033[1:32mO\033[m \033[1:33m{emoji.emojize('\U0001f534', language='pt')}\033[m \033[1:32mvenceu!\033[m ')
                lista.clear()
                break
            if X == 0:
                print('\n\033[1:31mTODOS PERDERAM!\033[m')
                break
            while X < 1 and X > 9 and X != 999:
                print('\n\033[1:31:40mOpção Inválida!\033[m')
                X = int(input(f'\n\033[1:34mDigite a posição\033[m \033[1:33m{emoji.emojize('\u274C', language='pt')}\033[m\033[1:34m: \033[m'))
            for c in lista:
                for i in range(0,3):
                    if c[i] == X:
                        c[i] = f'\033[1:31m{'X':^15}\033[m'
            print('')
        elif quem_comeca == 2:
            O = int(input(f'\n\033[1:34mDigite a posição\033[m \033[1:33m{emoji.emojize('\U0001f534',language= 'pt')}\033[m\033[1:34m: \033[m'))
            if O == 999:
                print(f'\n\033[1:32mO\033[m \033[1:33m{emoji.emojize('\u274C',language= 'pt')}\033[m \033[1:32mvenceu!\033[m ')
                lista.clear()
                break
            if O == 0:
                print('\n' + ' ' * 11 + '\033[1:31:40mNINGUÉM GANHOU!\033[m')
                break
            while O < 1 and O > 9 and O != 999:
                print('\n\033[1:31:40mOpção Inválida!\033[m')
                O = int(input(f'\n\033[1:34mDigite a posição\033[m \033[1:33m{emoji.emojize('\U0001f534', language='pt')}\033[m\033[1:34m: \033[m'))
            for c in lista:
                for i in range(0, 3):
                    if c[i] == O:
                        c[i] = f'\033[1:31m{'O':^15}\033[m'
            print('')
        if quem_comeca == 1:
            quem_comeca = 2
        elif quem_comeca == 2:
            quem_comeca = 1

while True:
    matrix_nula()
    quem_e_quem()
    jogando()
    lista.clear()
    resposta = str(input('\n\033[1:34mVocês querem jogar novamente?\033[m \033[1:35m[S/N]\033[m ')).strip().upper()[0]
    while resposta not in "SN":
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        resposta = str(input('\n\033[1:34mVocês querem jogar novamente?\033[m \033[1:35m[S/N]\033[m ')).strip().upper()[0]
    if resposta == 'N':
        time.sleep(1)
        print('\n' + ' ' * 12 + '\033[1:32:40mVOLTEM SEMPRE!\033[m')
        break