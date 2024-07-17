def contador(i,f,p):
    """
    --> Faz uma contagem e mostra na tela.
    :parâmetro i: início da contagem.
    :parâmetro f: fim da contagem.
    :parâmetro p: passo da contagem.
    :return: sem retorno.
    Função criada por Gustavo Guanabara do Canal Curso em Vídeo.
    """
    c = i
    while c <= f:
        print(f'{c}', end=', ', flush=True)
        c += p
    print('Fim!')


contador(2, 10, 2)
help(contador)
input('\n\033[1:34mDigite "sair" para sair: \033[m')