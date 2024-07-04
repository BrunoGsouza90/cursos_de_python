nota1 = float(input('\nDigite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('\n\033[1:31mReprovado!\033[m')
    print('Sua média foi de \033[31m{}\033[m!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('\n\033[1:33mEm recuperação!\033[m')
    print('Sua média foi de \033[33m{}\033[m!'.format(media))
else:
    print('\n\033[1:32mAprovado!\033[m')
    print('Sua média foi de \033[32m{}\033[m!'.format(media))
input('\n\033[1:34mDigite "sair" para sair: \033[m')