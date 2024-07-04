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
    termos = 10
    while termos != 0:
        passo = 0
        while passo < termos:
            print('\033[1:31m',primeiro_termo, end=' → \033[m')
            primeiro_termo += + razao
            passo += 1
        print('\033[1:31:40m=-=-=Fim=-=-=\033[m')
        termos = int(input('\n\033[1:31mVocê deseja ver mais quantos termos?\033[m '))
elif modo == 2:
    termos = 10
    while termos != 0:
        passo = 0
        while passo < termos:
            print('\033[1:31m',primeiro_termo, end=' → \033[m')
            primeiro_termo -= razao
            passo += 1
        print('\033[1:31:40m=-=-=Fim=-=-=\033[m')
        termos = int(input('\n\033[1:31mVocê deseja ver mais quantos termos?\033[m '))
else:
    termos = 10
    while termos != 0:
        passo = 0
        while passo < termos:
            print('\033[1:31m',primeiro_termo, end=' → \033[m')
            passo += 1
        print('\033[1:31:40m=-=-=Fim=-=-=\033[m')
        termos = int(input('\n\033[1:31mVocê deseja ver mais quantos termos?\033[m '))
input('\n\033[1:34mDigite "sair" para sair: \033[m')