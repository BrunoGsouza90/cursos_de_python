def teste():
    x = 8
    print(f'Na função teste n vale "{n}" !')
    print(f'Na função teste x vale "{x}" !')
n = 2
print(f'No programa principal, "n" vale "{n}" !')
# print(f'No programa principal, "x" vale "{x}" !')
# --> Erro: A variável "x" global não foi informada, apenas a variável "x" local.
teste()

print('')


def funcao():
    n1 = 4
    print(f'"n1" local vale {n1} !')


n1 = 2
funcao()
print(F'"n1" global vale {n1} !')

print('')


def funcao():
    global n1
    print(f'"n1" local vale {n1} !')


n1 = 2
funcao()
print(F'"n1" global vale {n1} !')


def funcao():
    global n1
    n1 = 4
    print(f'"n1" local vale {n1} !')


n1 = 2
funcao()
print(F'"n1" global vale {n1} !')

input('\n\033[1:34mDigite "sair" para sair: \033[m')