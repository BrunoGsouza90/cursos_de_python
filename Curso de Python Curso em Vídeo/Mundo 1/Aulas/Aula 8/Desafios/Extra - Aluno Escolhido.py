import random
aluno1 = str(input('Aluno 1: '))
aluno2 = str(input('Aluno 2: '))
aluno3 = str(input('Aluno 3: '))
aluno4 = str(input('Aluno 4: '))
lista = [aluno1, aluno2, aluno3,aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi o \033[31m{}\033[m!'.format(escolhido))
input('\n\033[1:34mDigite "sair" para sair: \033[m')