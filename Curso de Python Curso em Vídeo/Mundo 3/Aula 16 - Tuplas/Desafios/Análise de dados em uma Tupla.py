tupla = []
pares = []
for cont in range(1,5):
    num = int(input(f'\n\033[1:34mDigite o {cont}° Número:\033[m '))
    tupla.append(num)
    if num % 2 == 0:
        pares.append(str(num))
tupla = tuple(tupla)
nove = tupla.count(9)
if 3 in tupla:
    tres = tupla.index(3)
    print(f'\n\033[1:31mO primeiro valor\033[m \033[1:33m"3"\033[m \033[1:31mfoi digitado na\033[m \033[1:33m{tres}°\033[m \033[1:31mposição!\033[m')
else:
    print('\n\033[1:31mNão existe o valor\033[m \033[1:33m"3"\033[m \033[1:31mna tupla!\033[m')
print(f'\033[1:31mOs números da tupla são:\033[m\033[1:33m',*tupla,f'\033[m\033[1:31m!\033[m')
print(f'\033[1:31mO valor\033[m \033[1:33m"9"\033[m \033[1:31mapareceu na tupla\033[m \033[1:33m{nove}\033[m \033[1:31mvezes!\033[m')
print(f'\033[1:31mOs números pares são os\033[m \033[1:33m{' '.join(pares)}\033[m\033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')