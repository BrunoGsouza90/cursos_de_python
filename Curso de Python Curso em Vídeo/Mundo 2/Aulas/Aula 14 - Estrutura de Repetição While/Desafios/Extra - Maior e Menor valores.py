import emoji

continuar = 'Sim'
soma = 0
maior = 0
menor = 0
quantidade_valores = 0
while continuar != 'Não':
    valor = int(input('\n\033[1:34mDigite um número:\033[m '))
    soma += valor
    quantidade_valores += 1
    if quantidade_valores == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    continuar = str(input('\n\033[1:32mQuer continuar?\033[m\n\033[1:34mDigite "Sim ou "Não:\033[m ')).strip().title()
    while continuar != 'Sim' and continuar != 'Não':
        print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
        continuar = str(input('\n\033[1:32mQuer continuar?\033[m\n\033[1:34mDigite "Sim ou "Não:\033[m ')).strip().title()
print('\n\033[1:31mO maior valor é o\033[m \033[1:33m{}\033[m \033[1:31me o menor valor é o\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(maior,menor))
print('\033[1:31mForam digitados\033[m \033[1:33m{}\033[m \033[1:31mnúmeros e a média deles é\033[m \033[1:33m{:.2f}\033[m\033[1:31m!\033[m'.format(quantidade_valores,soma / quantidade_valores))
input('\n\033[1:34mDigite "sair" para sair: \033[m')