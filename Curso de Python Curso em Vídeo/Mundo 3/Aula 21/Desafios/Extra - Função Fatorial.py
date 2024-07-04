def fatorial(numero, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número específico.
    """
    print('')
    contador = 1
    for c in range(numero, 0, -1):
        if show:
            print(f'\033[1:33m{c}\033[m', end='')
            if c > 1:
                print(' \033[1:31mx\033[m ', end='')
            else:
                print(' \033[1:31m=\033[m ', end='')
        contador *= c
    return f'\033[1:32m{contador}\033[m'

print(fatorial(5, show=True))

input('\n\033[1:34mDigite "sair" para sair: \033[m')