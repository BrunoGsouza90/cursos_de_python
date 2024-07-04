termos = int(input('\n\033[4:31m=-=-=-=-=-=-=Sequência de Fibonacci-=-=-=-=-=-=\033[m\n\n\033[1:34mQuantidade de termos:\033[m '))
t1 = 0
t2 = 1
if termos == 1:
    print('\033[1:31m0 →\033[m', end='')
elif termos == 2:
    print('\033[1:31m0 → 1 →\033[m', end='')
else:
    print('\033[1:31m0 → 1 →\033[m', end='')
    cont = 2
    while cont < termos:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print('\033[1:31m', t3, end=' →\033[m')
        cont += 1
print('\033[1:32m Acabou\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')