passo = produto = preco = soma = preco_maior = barato = valor = continuar = 0
while True:
    passo += 1
    print(f'\n         \033[1:35:40m{passo}° PRODUTO\033[m')
    produto = str(input(f'\n\033[1:34mDigite o nome do {passo}° Produto:\033[m ')).strip().title()
    preco = float(input(f'\033[1:34mDigite o preço do {passo}° Produto:\033[m '))
    soma += preco
    if preco > 1000.00:
        preco_maior += 1
    if passo == 1:
        mais_barato = produto
    else:
        if preco < valor:
            mais_barato = produto
    continuar = str(input('\033[1:34mVocê deseja continuar?\033[m \033[1:35m[S/N]\033[m ')).strip().title()
    while continuar not in 'SsNn':
        print('\033[1:31:40mOpção Inválida!\033[m')
        continuar = str(input('\n\033[1:34mVocê deseja continuar?\033[m \033[1:35m[S/N]\033[m ')).strip().title()
    if continuar in 'Nn':
        break
print(f'\033[1:31mA soma de todos os produtos é\033[m \033[1:33m{soma}\033[m\033[1:31m!\033[m')
print(f'\033[1:33m{preco_maior}\033[m \033[1:31mprodutos custam mais de R$ 1000.00!\033[m')
print(f'\033[1:31mO produto mais barato é o\033[m \033[1:33m"{mais_barato}"\033[m\033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')