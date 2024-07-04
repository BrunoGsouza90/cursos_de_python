def notas(*num, sit=False):
    '''
    --> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    cont = 1
    lista_nota = list()
    while True:
        numeros = float(input(f'\n\033[1:34mDigite o {cont}º Número: \033[m'))
        lista_nota.append(numeros)
        resposta = str(input('\n\033[1:34mQuer digitar mais um número? [S/N] \033[m')).strip().upper()[0]
        while resposta not in 'SN':
            print('\n\033[1:31mOpção Inválida!')
            resposta = str(input('\n\033[1:34mQuer digitar mais um número? [S/N] \033[m')).strip().upper()[0]
        if resposta == 'N':
            break
        cont += 1
    resposta = str(input('\n\033[1:34mQuer mostrar a situação? [S/N] \033[m')).strip().upper()[0]
    while resposta not in 'SN':
        print('\n\033[1:31mOpção Inválida!')
        resposta = str(input('\n\033[1:34mQuer mostrar a situação? [S/N] \033[m')).strip().upper()[0]
    if resposta == 'S':
        sit = True
    else:
        sit = False
    total = len(lista_nota)
    soma = 0
    maior = menor = lista_nota[0]
    for nota in lista_nota:
        soma += nota
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    media = soma / total
    if soma < 7:
        situacao = 'Ruim'
    elif soma == 7:
        situacao = 'Média'
    else:
        situacao = 'Boa'
    if sit:
        dicionario = {
            'Total de Notas': total,
            'Maior Nota': maior,
            'Menor Nota': menor,
            'Média das Notas': f'{media:.2f}',
            'Situação': situacao,
        }
        return dicionario
    else:
        dicionario = {
            'Total de Notas': total,
            'Maior Nota': maior,
            'Menor Nota': menor,
            'Média das Notas': f'{media:.3f}',
        }
        return dicionario

help(notas)
resposta = notas()
print(resposta)
input('\n\033[1:34mDigite "sair" para sair: \033[m')