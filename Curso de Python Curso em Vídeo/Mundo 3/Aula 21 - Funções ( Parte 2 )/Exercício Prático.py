def Fatorial(num=1):
    fatorial = 1
    for contador in range(num, 0, -1):
        fatorial *= contador
    return fatorial


numero = int(input('\nDigite um número: '))
print(f'O fatorial de {numero} é {Fatorial(numero)} !')

f1 = Fatorial(5)
f2 = Fatorial(4)
f3 = Fatorial()
print(f'Os resultados são {f1}, {f2}, {f3} !')


def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('\nDigite um número: '))
if parOuImpar(num):
    print('O número é Par!')
else:
    print('O número é Ímpar!')
input('\n\033[1:34mDigite "sair" para sair: \033[m')