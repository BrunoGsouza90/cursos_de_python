def notas(situacao = False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = {}
    lista = []
    cont = 1
    while True:
        nota = float(input(f'\n\033[1:34mDigite a {cont}º nota: \033[m'))
        lista.append(nota)
        resposta = str(input('\n\033[1:34mTem mais notas? [S/N] \033[m')).strip().upper()[0]
        while resposta not in 'SN':
            print('\n\033[1:31mOpção Inválida!')
            resposta = str(input('\n\033[1:34mTem mais notas? [S/N] \033[m')).strip().upper()[0]
        if resposta == 'N':
            break
    dicionario['Total de Notas'] = len(lista)
    dicionario['Maior Nota'] = max(lista)
    dicionario['Menor Nota'] = min(lista)
    dicionario['Média das Notas']= sum(lista)/len(lista)
    resposta = str(input('\n\033[1:34mQuer apresentar a situação? [S/N] \033[m')).strip().upper()[0]
    while resposta not in 'SN':
        print('\n\033[1:31mOpção Inválida!')
        resposta = str(input('\n\033[1:34mQuer aprensentar a situação? [S/N] \033[m')).strip().upper()[0]
    if resposta == 'S':
        if dicionario['Média das Notas'] < 7:
            dicionario['Situação'] = 'Ruim'
        elif dicionario['Média das Notas'] == 7:
            dicionario['Situação'] = 'Razoável'
        else:
            dicionario['Situação'] = 'Boa'
    return f'\033[1:33m{dicionario}\033[m'

print(notas())
input('\n\033[1:34mDigite "sair" para sair: \033[m')