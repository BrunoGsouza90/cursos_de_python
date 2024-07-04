num = int(input('\n\033[1:34mDigite um número:\033[m '))
final = 0
fatorial = 1
print('\n\033[1:35m{}!\033[m\033[1:31m ='.format(num),end=' ')
while final < num:
    fatorial *= num
    print('{}'.format(num),end=' ')
    print('x' if num > 1 else '=',end=' ')
    num -= 1
print('\033[m\033[1:32m{}\033[m'.format(fatorial))

num = int(input('\n\033[1:34mDigite um número:\033[m '))
print('\n\033[1:35m{}!\033[m\033[1:31m ='.format(num),end=' ')
fatorial = 1
for c in range(0,num):
    print('{}'.format(num), end=' ')
    print('x' if num > 1 else '=', end=' ')
    fatorial *= num
    num -= 1
print('\033[m\033[1:32m{}\033[m'.format(fatorial))
input('\n\033[1:34mDigite "sair" para sair: \033[m')