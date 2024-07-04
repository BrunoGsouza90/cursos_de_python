num = int(input('\nDigite um número inteiro: '))
print('\nPara transformar seu número em \033[1:33m"binário"\033[m. \033[1:35mDigite 1\033[m... ')
print('Para transformar seu número em \033[1:33m"octal"\033[m. \033[1:35mDigite 2\033[m... ')
print('Para transformar seu número em \033[1:33m"hexadecimal"\033[m. \033[1:35mDigite 3\033[m... ')
opcao = int(input('\n\033[4:36mDigite aqui:\033[m '))
if opcao == 1:
    print('\nO número digitado em \033[1:33mbinário\033[m é \033[1:31m{}\033[m!'.format(bin(num)[2:]))
elif opcao == 2:
    print('\nO número digitado em \033[1:33mbinário\033[m é \033[1:31m{}\033[m!'.format(oct(num)[2:]))
elif opcao == 3:
    print('\nO número digitado em \033[1:33mbinário\033[m é \033[1:31m{}\033[m!'.format(hex(num)[2:]))
else:
    print('\n\033[1:31:40mOpção Inválida!\033[m')

input('\n\033[1:34mPara "sair" digite sair: \033[m')