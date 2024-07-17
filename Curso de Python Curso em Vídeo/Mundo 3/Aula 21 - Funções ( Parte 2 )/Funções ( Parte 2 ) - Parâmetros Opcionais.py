def somar(a, b, c=0):
    """
    --> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor.
    :param b: O segundo valor.
    :param c: O terceiro valor.
    Função criada por Gustavo Guanabara do Canal Curso em Vídeo.
    """
    soma = a + b + c
    print(f'A soma vale {soma} !')


somar(3, 2, 5)
somar(8, 4)

input('\n\033[1:34mDigite "sair" para sair: \033[m')