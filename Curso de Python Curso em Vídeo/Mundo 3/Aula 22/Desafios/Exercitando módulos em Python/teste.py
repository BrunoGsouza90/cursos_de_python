import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é R${moeda.metade(preco)}!')
print(f'A dobro de {preco} é R${moeda.dobro(preco)}!')
print(f'Aumentando 10%, temos R${moeda.aumentar(preco, 10)}!')
print(f'Diminuindo 13%, temos R${moeda.diminuir(preco, 13)}!')

input('\033[1:34mDigite "sair" para sair: \033[m')