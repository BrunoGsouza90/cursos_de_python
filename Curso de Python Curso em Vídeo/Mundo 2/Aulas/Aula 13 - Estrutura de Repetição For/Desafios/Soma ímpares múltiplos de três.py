print('\n\033[1:31:40mSoma ímpares múltiplos de três\033[m\n')
partida = 1
soma = 0
for c in range(0,500):
    if partida % 3 == 0:
        print('            \033[1:33m{}\033[m'.format(partida))
        soma = partida + soma
        partida = partida + 1
    else:
        partida = partida + 1
        soma = soma
print('      \033[1:34mResultado\033[m: \033[31m{}\033[m'.format(soma))
input('\n\033[1:34mPara "sair" digite sair : \033[m')