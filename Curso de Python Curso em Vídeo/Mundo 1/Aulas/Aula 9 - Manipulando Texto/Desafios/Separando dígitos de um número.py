num = str(input('Digite um número de 0 a 9999: '))
unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]
print('A unidade do número é: {}! \nA dezena do número é: {}! \nA centena do número é: {}! \nO milhar do número é: {}!'.format(unidade,dezena,centena,milhar))

num1 = int(input('Digite um número: '))
unidade = num1 // 1 % 10
dezena = num1 // 10 % 10
centena = num1 // 100 % 10
milhar = num1 // 1000 % 10
print('A unidade do número é: {}! \nA dezena do número é: {}! \nA centena do número é: {}! \nO milhar do número é: {}!'.format(unidade,dezena,centena,milhar))
input('Digite "sair" para sair: ')