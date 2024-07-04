import time,emoji
num1 = int(input('\n\033[1:34mDigite o primeiro número:\033[m '))
num2 = int(input('\033[1:34mDigite o segundo número:\033[m '))
opcao = 0
while opcao != 5:
    print('\n\033[1:31:40m====Menu de Opções====\033[m')
    print('''\n\033[1:31m[1]\033[m \033[1:33mSomar\033[m
\033[1:31m[2]\033[m \033[1:33mMultiplicar\033[m
\033[1:31m[3]\033[m \033[1:33mMaior\033[m
\033[1:31m[4]\033[m \033[1:33mNovos números\033[m
\033[1:31m[5]\033[m \033[1:32mSair do Progama\033[m''')
    opcao = int(input('\n\033[1:34mDigite a Opção Que Deseja:\033[m '))
    while opcao < 1 or opcao > 5:
        print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
        time.sleep(2)
        opcao = 0
    if opcao == 1:
        print('\n\033[1:31m{}\033[m + \033[1:31m{}\033[m = \033[1:33m{}\033[m'.format(num1,num2,num1 + num2))
        time.sleep(2)
    elif opcao == 2:
        print('\n\033[1:31m{}\033[m * \033[1:31m{}\033[m = \033[1:33m{}\033[m'.format(num1,num2,num1 * num2))
        time.sleep(2)
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('\n\033[1:31mO número maior é o\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(maior))
        time.sleep(2)
    elif opcao == 4:
        num1 = int(input('\n\033[1:34mDigite o primeiro número:\033[m '))
        num2 = int(input('\033[1:34mDigite o segundo número:\033[m '))
        print('\033[1:31mOs novos números agora são\033[m \033[1:33m{}\033[m \033[1:31me\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(num1,num2))
print('\n\033[1:35mFINALIZANDO O PROGAMA...\033[m')
time.sleep(2)
print('\033[1:31mFim do Progama! Volte Sempre...\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')