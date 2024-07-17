import emoji
primeiro_termo = int(input('\n\033[1:34mDigite o primeiro termo da PA:\033[m '))
razao = int(input('\033[1:34mDigite a razão:\033[m '))
print('')
ultimo_termo = primeiro_termo + (11 - 1) * razao
for c in range(primeiro_termo,ultimo_termo,razao):
    print('\033[1:31m',c, end=' → \033[m')
print('\033[1:31:40m=-=-=Fim=-=-=\033[m')

primeiro_termo = int(input('\n\033[1:34mDigite o primeiro termo da PA:\033[m '))
ultimo_termo = primeiro_termo + 10
razao = int(input('\033[1:34mDigite a razão:\033[m '))
print('''\n\033[1:31m[1]\033[m \033[1:33mCrescente\033[m
\033[1:31m[2]\033[m \033[1:33mDecrescente\033[m
\033[1:31m[3]\033[m \033[1:33mConstante\033[m''')
modo = int(input('\n\033[1:34mDigite o modo que deseja:\033[m '))
while modo < 1 or modo > 3:
    print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
    modo = int(input('\n\033[1:34mDigite o modo que deseja:\033[m '))
    print('')
if modo == 1:
    for c in range(primeiro_termo,ultimo_termo):
        print('\033[1:31m',primeiro_termo, end=' → \033[m')
        primeiro_termo += razao
    print('\033[1:31:40m=-=-=Fim=-=-=\033[m')
elif modo == 2:
    for c in range(primeiro_termo,ultimo_termo):
        print(primeiro_termo, end=' → ')
        primeiro_termo = primeiro_termo - razao
    print('\033[1:31:40m=-=-=Fim=-=-=\033[m')
else:
    for c in range(primeiro_termo,ultimo_termo):
        print(primeiro_termo, end=' → ')
    print('\033[1:31:40m=-=-=Fim=-=-=\033[m')

primeiro_termo = int(input('\n\033[1:34mDigite o primeiro termo:\033[m '))
razao = int(input('\033[1:34mDigite a razão:\033[m '))
print('''\n\033[1:31m[1]\033[m \033[1:33mCrescente\033[m
\033[1:31m[2]\033[m \033[1:33mDecrescente\033[m
\033[1:31m[3]\033[m \033[1:33mConstante\033[m''')
modo = int(input('\n\033[1:34mDigite o modo que deseja:\033[m '))
print('')
while modo < 1 or modo > 3:
    print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
    modo = int(input('\n\033[1:34mDigite o modo que deseja:\033[m '))
if modo == 1:
    passo = 0
    while passo < 10:
        print('\033[1:31m',primeiro_termo, end=' → \033[m')
        primeiro_termo += + razao
        passo += 1
    print('\033[1:31:40m=-=-=Fim=-=-=\033[m')
elif modo == 2:
    passo = 0
    while passo < 10:
        print('\033[1:31m',primeiro_termo, end=' → \033[m')
        primeiro_termo -= razao
        passo += 1
    print('\033[1:31:40m=-=-=Fim=-=-=\033[m')
else:
    passo = 0
    while passo < 10:
        print('\033[1:31m',primeiro_termo, end=' → \033[m')
        passo += 1
    print('\033[1:31:40m=-=-=Fim=-=-=\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')