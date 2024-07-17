valor = cont = 0
while True:
    valor = int(input('\n\033[1:34mDigite o número que quer ver a tabuada:\033[m '))
    print('\033[1:31mPara sair do progama digite um número negativo!\033[m\n')
    if valor < 0:
        break
    cont = 0
    while cont < 11:
        print(f'{valor} x {cont:2} = {valor*cont}')
        cont += 1
input('\n\033[1:34mDigite "sair" para sair: \033[m')