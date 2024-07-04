def leiaInt(num):
    num = input(num)
    while len(num) > 1 or len(num) == 0 or num not in '123456789':
        while len(num) == 0:
            print('\n\033[1:31mOpção Inválida!\033[m')
            num = input('\n\033[1:34mDigite um número por favor: \033[m')
        while not num.isnumeric():
            print('\n\033[1:31mOpção Inválida!\033[m')
            num = input('\n\033[1:34mDigite um número inteiro: \033[m')
        while num.isnumeric() and len(num) > 1:
            print('\n\033[1:31mOpção Inválida!\033[m')
            num = input('\n\033[1:34mDigite um número com apenas uma casa: \033[m')
    return num


n = leiaInt(f'\n\033[1:34mDigite um número: \033[m')
print(f'\n\033[1:31mVocê acabou de digitar o número:\033[m \033[1:33m{n}\033[m \033[1:31m! \033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')