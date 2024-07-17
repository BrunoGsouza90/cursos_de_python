tempo = int(input('Quantos anos teu seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro está velho!')

nome = str(input('Digite seu primeiro nome: '))
print('Verificando se seu nome é "Alberto": ')
print('Sim! Seu nome é Alberto!' if nome == 'Alberto' else 'Não! Seu nome não é Alberto!')
print('--FIM--')
input('Digite "sair" para sair: ')