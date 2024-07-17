primeiro_termo = int(input('\n\033[1:34mDigite o primeiro termo:\033[m '))
razao = int(input('\033[1:34mDigite a razão:\033[m '))
termo = 10
contador = 0
print('')
while termo != 0:
    print('\033[1:31m', primeiro_termo, end=' ''→\033[m ')
    primeiro_termo += razao
    termo -= 1
    contador += 1
    if termo == 0:
        print('\033[1:31mPausa\033[m')
        termo = int(input('\n\033[1:31mVocê deseja ver mais quantos termos?\033[m '))
print('\n\033[1:32mForam apresentados\033[m \033[1:33m{}\033[m \033[1:32mtermos nessa PA!\033[m'.format(contador))
print('\n\033[1:31:40m=-=-=Fim do Progama=-=-=\033[m')
input('\n\n\033[1:34mDigite "sair" para sair: \033[m')