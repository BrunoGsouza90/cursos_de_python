from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}!')
print(f'O dobro de {num} é {numeros.dobro(num)}!')

input('\n\033[1:34mDigite "sair" para sair: \033[m')