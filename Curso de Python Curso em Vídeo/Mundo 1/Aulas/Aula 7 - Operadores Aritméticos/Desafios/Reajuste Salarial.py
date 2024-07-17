salario=float(input('\nDigite o seu salário: \033[32mR$\033[m '))
print('O seu salário com \033[33m15%\033[m de aumento é \033[31mR$ {:.2f}\033[m!'.format(salario+(15*salario/100)))
input('\n\033[1:34mDigite "sair" para sair: \033[m')