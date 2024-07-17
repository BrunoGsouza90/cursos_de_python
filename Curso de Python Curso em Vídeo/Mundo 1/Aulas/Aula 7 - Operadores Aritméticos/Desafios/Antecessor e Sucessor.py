cores = {'limpa':'\033[m','vermelho':'\033[31m','azul_negrito':'\033[1:34m'}
num = int(input('\nDigite um número: '))
print('O antecessor de {}{}{} é {}{}{}, e o seu sucessor é {}{}{}!'.format(cores['vermelho'],num,cores['limpa'],cores['vermelho'],num-1,cores['limpa'],cores['vermelho'],num+1,cores['limpa']))
input('\n{}Digite "sair" para sair: {}'.format(cores['azul_negrito'],cores['limpa']))