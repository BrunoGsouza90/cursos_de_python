nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
ultimo = nome[-1]
print('O seu primeiro nome é: {}!'.format(nome[0]))
print('O seu último nome é: {}!'.format(ultimo))
input('Digite "sair" para sair: ')