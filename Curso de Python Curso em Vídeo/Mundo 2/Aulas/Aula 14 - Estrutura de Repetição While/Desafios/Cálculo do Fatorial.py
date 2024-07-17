num = int(input('\n\033[1:34mDigite um numero: \033[m'))
total = num
fatorial = num - 1
while fatorial > 0:
    total *= fatorial
    fatorial -= 1
print('\n\033[1:31mO fatorial de\033[m \033[1:33m{}\033[m \033[1:31mé\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(num,total))

num = int(input('\n\033[1:34mDigite um numero: \033[m'))
total = num
final = num
fatorial = num - 1
for c in range(1,final):
    total *= fatorial
    fatorial -= 1
print('\n\033[1:31mO fatorial de\033[m \033[1:33m{}\033[m \033[1:31mé\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(num,total))