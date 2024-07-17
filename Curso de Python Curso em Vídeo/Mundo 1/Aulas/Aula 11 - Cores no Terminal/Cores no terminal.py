a = 3
b = 5
print('Os valores são \033[32m{} \033[me \033[31m{}\033[m!'.format(a,b))
nome = str(input('Digite seu nome: ')).strip().title()
print('Olá! É um prazer te conhecer \033[4:36m{}\033[m!'.format(nome))
input('\nDigite "sair" para sair: ')