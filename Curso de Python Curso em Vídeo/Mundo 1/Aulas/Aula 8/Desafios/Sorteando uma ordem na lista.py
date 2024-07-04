import random
aluno=str(input('Digite o nome do primeiro aluno: '))
print('É um prazer {}!'.format(aluno))
aluno1=str(input('Digite o nome do segundo aluno: '))
print('É um prazer {}!'.format(aluno1))
aluno2=str(input('Digite o nome do terceiro aluno: '))
print('É um prazer {}!'.format(aluno2))
aluno3=str(input('Digite o nome do quarto aluno: '))
print('É um prazer {}!'.format(aluno3))
lista = [aluno,aluno1,aluno2,aluno3]
sorteados = random.sample((lista),4)
print('A ordem de apresentação dos alunos de acordo com os números sorteados é: {}'.format(sorteados))

import random
aluno=str(input('Digite o nome do primeiro aluno: '))
print('É um prazer {}!'.format(aluno))
aluno1=str(input('Digite o nome do segundo aluno: '))
print('É um prazer {}!'.format(aluno1))
aluno2=str(input('Digite o nome do terceiro aluno: '))
print('É um prazer {}!'.format(aluno2))
aluno3=str(input('Digite o nome do quarto aluno: '))
print('É um prazer {}!'.format(aluno3))
lista = [aluno,aluno1,aluno2,aluno3]
random.shuffle(lista)
print('A ordem dos alunos para a apresentação é: {}!'.format(lista))
input('Digite sair para poder sair: ')