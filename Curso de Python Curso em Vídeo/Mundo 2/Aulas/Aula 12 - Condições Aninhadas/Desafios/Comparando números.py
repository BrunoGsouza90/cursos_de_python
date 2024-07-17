num1 = int(input('\nDigite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 > num2:
    print('\nO número \033[1:31m{}\033[m é maior que o número \033[1:31m{}\033[m!'.format(num1,num2))
elif num2 > num1:
    print('\nO número \033[1:31m{}\033[m é maior que o número \033[1:31m{}\033[m!'.format(num2,num1))
else:
    print('\nOs valores de ambos os números é \033[1:31m{}\033[m!'.format(num1))
input('\n\033[1:34mDigite "sair" para sair: \033[m')