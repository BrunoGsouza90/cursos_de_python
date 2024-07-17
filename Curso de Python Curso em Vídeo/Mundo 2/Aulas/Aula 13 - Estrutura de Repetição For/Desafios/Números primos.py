num = int(input('\nDigite um número inteiro: '))
if num == 1:
    print('\033[1:31m\nEsse número não é primo!\033[m')
elif num == 2 or num == 3 or num == 5 or num == 7 or num == 11 or num == 13 or num == 17 or num == 19:
    print('\033[1:32m\nEsse número é primo!\033[m')
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0 or num % 17 == 0 or num % 19 == 0:
    print('\033[1:31m\nEsse número não é primo!\033[m')
else:
    print('\033[1:32m\nEsse número é primo!\033[m')

num1 = int(input('\nDigite um número inteiro: '))
divisao = 2
fim = num1 - 3
primo = 0
for c in range(0,fim):
    if num1 % divisao == 0:
        primo = primo + 1
        divisao += 1
    else:
        divisao += 1
if primo > 0:
    print('\033[1:31m\nEsse número não é primo!\033[m')
else:
    print('\033[1:32m\nEsse número é primo!\033[m')
input('\n\033[1:34mPara "sair" digite sair : \033[m')