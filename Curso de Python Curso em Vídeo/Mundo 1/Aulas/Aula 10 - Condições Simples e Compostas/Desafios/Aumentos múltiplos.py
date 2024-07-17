salario = float(input('Digite o seu salário... R$'))
if salario > 1250.00:
    salario = salario + (salario * 10 / 100)
    print('O seu novo salário com 10% de aumento é de R${:.2f}'.format(salario))
else:
    salario = salario + (salario * 15 / 100)
    print('O seu novo salário com 15% de aumento é de R${:.2f}'.format(salario))
input('Digite "sair" para sair: ')