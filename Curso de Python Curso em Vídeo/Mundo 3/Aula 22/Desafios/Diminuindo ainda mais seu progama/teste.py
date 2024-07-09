import moeda

preco = float(input('\nDigite o preço: R$ '))
moeda.resumo(preco, 10, 13)

input('\033[1:34mDigite "sair" para sair: \033[m')