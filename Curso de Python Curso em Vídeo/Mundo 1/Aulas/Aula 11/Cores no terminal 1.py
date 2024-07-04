nome = str(input('Digite seu nome: '))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[0:32m'}
print('É um prazer te conhecer {}{}{}!'.format(cores['verde'],nome,cores['limpa']))