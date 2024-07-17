def maior(* nums):
    maior = 0
    for num in nums:
        if num > maior:
            maior = num
    print(f'\n\033[1:31mO maior valor é\033[m \033[1:33m{maior}\033[m \033[1:31m!\033[m')

lista = list()
while True:
    tamanho = int(input('\n\033[1:34mDigite o tamanho da lista: \033[m'))
    while len(lista) < tamanho:
        lista.append(int(input('\n\033[1:34mDigite um valor: \033[m')))
    if len(lista) == 0:
        print('\n\033[1:31mVocê não digitou nenhum valor! \033[m')
    else:
        maior(*lista)
        lista.clear()
    resposta = str(input('\n\033[1:34mQuer continuar? [S / N] \033[m')).strip().upper()[0]
    while resposta not in 'SN':
        print('\n\033[1:31mOpção Inválida! \033[m')
        resposta = str(input('\n\033[1:34mQuer continuar? [S / N] \033[m')).strip().upper()[0]
    if resposta == 'N':
        break

input('\n\033[1:34mDigite "sair" para sair: \033[m')