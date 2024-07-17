import random
jogo = 'Par','Ímpar'
computador = escolha = valor = cont = jogador = valor_computador = 0
while True:
    computador = random.randint(1,2)
    valor_computador = random.randint(1,10)
    escolha = str(input('\n\033[1:34mDigite "Par" ou "Ímpar":\033[m ')).strip().title()
    while escolha != "Par" and escolha != "Ímpar":
        print('\nOpção Inválida!')
        escolha = str(input('\n\033[1:34mDigite "Par" ou "Ímpar":\033[m ')).strip().title()
    valor = int(input('\n\033[1:34mDigite um valor:\033[m '))
    if escolha == 'Par':
        if (valor + valor_computador) % 2 == 0:
            print('\n\033[1:32mVocê Ganhou!\033[m')
            cont += 1
        else:
            print('\n\033[1:31mO Computador Ganhou!\033[m')
            break
    else:
        if (valor + valor_computador) % 2 == 0:
            print('\n\033[1:31mO Computador Ganhou!\033[m')
            break
        else:
            print('\n\033[1:32mVocê Ganhou!\033[m')
            cont += 1
print(f'\n\033[1:31mVocê Ganhou\033[m \033[1:33m{cont}\033[m \033[1:31mvezes!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')