import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}!')
print(f'A dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}!')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}!')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13))}!')

input('\033[1:34mDigite "sair" para sair: \033[m')