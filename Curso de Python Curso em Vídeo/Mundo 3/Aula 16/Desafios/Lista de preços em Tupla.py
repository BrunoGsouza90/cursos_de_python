tupla = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('\033[1:33m-\033[m' * 38)
print(f'\033[1:35m{'LISTA DE PREÇOS':^39}\033[m')
print('\033[1:33m-\033[m' * 38)
for itens in tupla:
    if type(itens) is str:
        print(f'\033[1:31m{itens}\033[m\033[1:33m{'.' * (28 - len(itens))}\033[m',end=' ')
    else:
        print(f'\033[1:32mR$ {itens:>6.2f}\033[m')
print('\033[1:33m-\033[m' * 38)
input('\n\033[1:34mDigite "sair" para sair: ')