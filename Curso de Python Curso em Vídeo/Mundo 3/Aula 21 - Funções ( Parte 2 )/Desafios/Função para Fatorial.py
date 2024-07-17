def fatorial(numero, show=False):
    '''
    --> Essa função calcula o fatorial de um número.
    :param numero: Valor que será calculado o fatorial.
    :param show: Caso queira mostrar a equação show=True, se não show=False .
    :return: Valor a ser retornado como resultado da conta.
    '''
    if numero < 0:
        conta = '\n\033[1:31mO número digitado é negativo: \033[m'
        return conta
    elif numero == 0 or numero == 1:
        conta = f'\n\033[1:33m{numero}! =\033[m \033[1:31m1\033[m'
        return conta
    else:
        contador = numero
        multiplicador = numero - 1
        conta = f'\033[1:35m{numero}!\033[m \033[1:31m =\033[m '
        if show:
            multiplicador_texto = multiplicador + 1
            for passo in range(0, multiplicador_texto):
                if multiplicador_texto == 1:
                    conta += f' \033[1:33m {multiplicador_texto}\033[m  \033[1:31m =\033[m '
                else:
                    conta += f' \033[1:33m {multiplicador_texto}\033[m  \033[1:31m x \033[m '
                multiplicador_texto -= 1
            for passo in range(0, multiplicador):
                contador *= multiplicador
                multiplicador -= 1
            conta += f' \033[1:32m {contador}\033[m '
            return conta
        else:
            for passo in range(0, multiplicador):
                contador *= multiplicador
                multiplicador -= 1
            return f'\033[1:35m{numero}!\033[m \033[1:31m=\033[m \033[1:33m{contador}\033[m'


help(fatorial)
numero = int(input('\n\033[1:34mDigite o número cujo deseja ver o fatorial: \033[m'))
print(fatorial(numero, show=False))

input('\n\033[1:34mDigite "sair" para sair: \033[m')