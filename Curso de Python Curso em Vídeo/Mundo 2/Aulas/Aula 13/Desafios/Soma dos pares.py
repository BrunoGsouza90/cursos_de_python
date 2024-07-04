num0 = int(input('\nDigite um número inteiro: '))
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite um número inteiro: '))
num3 = int(input('Digite um número inteiro: '))
num4 = int(input('Digite um número inteiro: '))
num5 = int(input('Digite um número inteiro: '))
lista_num = [num0,num1,num2,num3,num4,num5]
posicao = 0
soma = 0
for c in range(0,6):
    if lista_num[posicao] % 2 == 0:
        soma = lista_num[posicao] + soma
        posicao = posicao + 1
    else:
        posicao = posicao + 1
print('\033[1:31mTotal\033[m = \033[1:33m{}\033[m!'.format(soma))
input('\n\033[1:34mPara "sair" digite sair : \033[m')