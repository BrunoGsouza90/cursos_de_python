nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') #Python 3.6 →
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print('O %s tem %d anos.' % (nome, idade)) #Python 2

salario = 987.30
print(f'O nome `{nome:20} tem {idade} anos e ganha R$ {salario:.2f}')
print(f'O nome `{nome:^20} tem {idade} anos e ganha R$ {salario:.2f}')
print(f'O nome `{nome:>20} tem {idade} anos e ganha R$ {salario:.2f}')
print(f'O nome `{nome:->20} tem {idade} anos e ganha R$ {salario:.2f}')
print(f'O nome `{nome:<20} tem {idade} anos e ganha R$ {salario:.2f}')
print(f'O nome `{nome:-<20} tem {idade} anos e ganha R$ {salario:.2f}')

input('\033[1:34mDigite "sair" para sair: \033[m')