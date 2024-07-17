sexo = str(input('\nDigite o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\nSexo Incorreto. Digite o seu sexo: [M/F] ')).strip().upper()[0]
print('\nSeu sexo é "{}"!\nSexo registrado com sucesso.'.format(sexo))