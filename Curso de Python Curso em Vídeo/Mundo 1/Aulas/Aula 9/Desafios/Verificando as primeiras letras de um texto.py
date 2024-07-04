cidade = str(input('Digite o nome de uma cidade: '))
cidade = cidade.title()
cidade = cidade.split()
v_f = "Santo" in cidade[0]
print(v_f)

cidade1 = str(input('Digite o nome de uma cidade: ')).strip().capitalize()
print('Verificando se a cidade digitada começa com "São" ...')
v_f1 = cidade1[0:3] == 'São'
print('A resposta é: {}!'.format(v_f1))
input('Digite "sair" para sair: ')