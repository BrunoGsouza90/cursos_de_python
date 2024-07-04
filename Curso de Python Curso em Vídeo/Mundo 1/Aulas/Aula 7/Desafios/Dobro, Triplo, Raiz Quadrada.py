num = int(input('\nDigite um número: '))
print('O dobro de \033[31m{}\033[m é \033[31m{}\033[m.\nO triplo de \033[31m{}\033[m é \033[31m{}\033[m.\nA raiz quadrada de \033[31m{}\033[m é \033[31m{:.2f}\033[m.'.format(num,num*2,num,num*3,num,num**(1/2)))
input('\n\033[1:34mDigite "sair" para sair: \033[m')