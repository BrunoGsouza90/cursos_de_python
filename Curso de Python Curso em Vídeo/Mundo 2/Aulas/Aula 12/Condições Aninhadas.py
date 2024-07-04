nome = str(input('Qual é o seu nome? '))
if nome == 'Bruno':
    print('Seu nome é bacana demais!')
elif nome == 'Ana' or nome == 'Pedro' or nome == 'Lucas':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Roseli, Maria, Julia, Raiani':
    print('Belo nome feminino!')
else:
    print('Seu nome é normal!')
print('Tenha um bom dia, {}!'.format(nome))