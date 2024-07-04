n1 = int(input('\nDigite um valor: '))
print('\033[31m',type(n1),'\033[m')
n2 = int(input('Digite outro número por favor: '))
print('\033[31m',type(n2),'\033[m')
print('A soma de \033[31mn1\033[m + \033[31mn2\033[m é\033[33m',n1 + n2,'\033[m!')
soma = n1 + n2
print('A soma de \033[31m{}\033[m mais \033[31m{}\033[m é igual a \033[33m{}\033[m!' .format(n1,n2,soma))
print('\033[31m',type(soma),'\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')