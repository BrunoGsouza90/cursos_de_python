num = int(input('\nDigite o número que deseja ver a tabuada: '))
multiplicador = 1
total = 0
print('Segue abaixo a tabuada completa de \033[4:33m{}\033[m!\n'.format(num))
for c in range(0,10):
    print('{} x {:2} = \033[31m{}\033[m'.format(num,multiplicador,num * multiplicador))
    multiplicador = multiplicador + 1
input('\n\033[1:34mPara "sair" digite sair : \033[m')