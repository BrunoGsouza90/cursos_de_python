from datetime import date

data1 = int(input('\nDigite uma data de nascimento: '))
data2 = int(input('Digite uma data de nascimento: '))
data3 = int(input('Digite uma data de nascimento: '))
data4 = int(input('Digite uma data de nascimento: '))
data5 = int(input('Digite uma data de nascimento: '))
data6 = int(input('Digite uma data de nascimento: '))
data7 = int(input('Digite uma data de nascimento: '))
datas = [data1,data2,data3,data4,data5,data6,data7]
ano_atual = date.today().year
posicao = 0
maioridade = 0
menoridade = 0
for c in range(0,7):
    if ano_atual - datas[posicao] < 21:
        menoridade += 1
        posicao += 1
    else:
        maioridade += 1
        posicao += 1
print('\n\033[1:31m{}\033[m \033[1:33mpessoas são de maioridade!\033[m'.format(maioridade))
print('\033[1:31m{}\033[m \033[1:33mpessoas são de menoridade!\033[m'.format(menoridade))
input('\n\033[1:34mPara "sair" digite sair : \033[m')