def lin():
    print('-' * 30)


lin()
print('        Curso em Vídeo   ')
lin()
print('        Aprenda Python   ')
lin()
print('       Gustavo Guanabara   ')
lin()


def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('Sistema de alunos'.center(30))
mensagem('Bruno Gonçalves de Souza'.center(30))


def soma(a,b):
    s = a + b
    print(f'A soma de {a} + {b} = {s} !')


soma(2,4)
soma(3,4)
soma(4,4)

def contador(*num):
    s = sum(num)
    print(f'A soma de {num} é {s} !')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print('')


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
print('')


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s} !')


soma(5, 2)
soma(2, 9, 4)
input('\n\033[1:34mDigite "sair" para sair: \033[m')