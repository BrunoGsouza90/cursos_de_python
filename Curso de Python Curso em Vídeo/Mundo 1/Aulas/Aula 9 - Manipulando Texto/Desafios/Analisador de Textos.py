nome = str(input('Digite seu nome completo: '))
maiusculas = nome.upper()
print('Seu nome em letras maiúsculas é: {}!'.format(maiusculas))
minusculas = nome.lower()
print('Seu nome em letras minúsculas é: {}!'.format(minusculas))
nome_dividido = nome.split()
quantidade = len(''.join(nome.split()))
print('Seu nome tem {} letras.'.format(quantidade))
print('O seu primeiro nome tem {} letras!'.format(len(nome_dividido[0])))

nome1 = str(input('Digite outro nome: ')).strip()
print('O nome digitado tem {} letras!'.format(len(nome1)-nome1.count(' ')))
print('O primeiro nome digitado tem {} letras!'.format(nome1.find(' ')))
input('Digite "sair" para sair: ')