peso1 = float(input('\nDigite um peso: '))
peso2 = float(input('Digite um peso: '))
peso3 = float(input('Digite um peso: '))
peso4 = float(input('Digite um peso: '))
peso5 = float(input('Digite um peso: '))
pesos = [peso1,peso2,peso3,peso4,peso5]
maior = 0
menor = 0
posicao = 0
posicao1 = 1
for c in range(0,4):
    if pesos[posicao] > pesos[posicao1]:
        maior = pesos[posicao]
        posicao1 += 1
    else:
        maior = pesos[posicao1]
        posicao = posicao1
        posicao1 += 1
posicao = 0
posicao1 = 1
for c in range(0,4):
    if pesos[posicao] < pesos[posicao1]:
        menor = pesos[posicao]
        posicao1 += 1
    else:
        menor = pesos[posicao1]
        posicao = posicao1
        posicao1 += 1
print('\n\033[1:31mO maior peso digitado foi o \033[1:33m{:.2f}\033[m\033[1:31m!\033[m'.format(maior))
print('\033[1:31mO menor peso digitado foi o \033[1:33m{:.2f}\033[m\033[1:31m!\033[m'.format(menor))
input('\n\033[1:34mPara "sair" digite sair : \033[m')