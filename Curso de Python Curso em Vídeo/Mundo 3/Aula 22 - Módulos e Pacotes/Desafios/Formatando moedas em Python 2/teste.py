import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} {moeda.metade(preco, True)}!')
print(f'A dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}!')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}!')
print(f'Diminuindo 13%, temos {moeda.diminuir(preco, 13, True)}!')

input('\033[1:34mDigite "sair" para sair: \033[m')