num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))
if num1 > num2 and num1 > 3:
    maior = num1
elif num2 > num3 and num2 > num1:
    maior = num2
else:
    maior = num3
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num3 and num2 < num1:
    menor = num2
else:
    menor = num3
print('O número maior é o {}, e o menor é o {}!'.format(maior,menor))
input('Digite "sair" para sair: ')