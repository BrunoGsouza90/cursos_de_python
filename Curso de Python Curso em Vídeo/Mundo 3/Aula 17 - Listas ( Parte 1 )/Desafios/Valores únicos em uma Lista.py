lista = []
cont = 1
while True:
    num = int(input(f'\n\033[1:34mDigite {cont}° valor: \033[m'))
    if num in lista:
        print('\n\033[1:31mEsse número já foi adicionado!\033[m')
    else:
        lista.append(num)
        print('\n\033[1:32mNúmero adicionado com sucesso!\033[m')
    cont += 1
    resposta = str(input(f'\n\033[1:34mQuer continuar? [S/N]: \033[m')).strip().upper()[0]
    while resposta not in 'SN':
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        resposta = str(input(f'\n\033[1:34mQuer continuar? [S/N]: \033[m')).strip().upper()[0]
    if resposta == 'N':
        break
lista.sort()
print(f'\n\033[1:31mA lista digitada foi:\033[m \033[1:33m{lista}\033[m \033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')