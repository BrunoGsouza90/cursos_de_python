def somar(a=0, b=0, c=0):
    soma = a + b + c
    print(f'A soma vale {soma} !')


somar(3, 2, 5)
somar(2, 2)
somar(4)


print('')


def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma


print(somar(3, 2, 5))
print(somar(2, 2))
resposta = somar(4)
print(resposta)

input('\n\033[1:34mDigite "sair" para sair: \033[m')