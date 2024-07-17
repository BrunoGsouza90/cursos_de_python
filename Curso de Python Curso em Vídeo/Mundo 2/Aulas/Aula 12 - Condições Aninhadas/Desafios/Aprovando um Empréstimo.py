import time

nome = str(input('\nDigite o seu nome: '))
print('\nÉ um prazer \033[1:31m{}\033[m! Bem-Vindo ao \033[1:35mBanco S.A\033[m'.format(nome))
valor = float(input('\nDigite o valor da casa que deseja fazer o empréstimo: \033[32mR$ \033[m'))
salario = float(input('Digite o seu salário: \033[32mR$ \033[m'))
parcelas = int(input('Digite em quantas vezes você vai pagar: '))

print('\033[1:35m\nPROCESSANDO...\033[m\n')
time.sleep(2)

if valor / parcelas <= salario * 30 / 100:
    prestacao_mensal = valor / parcelas
    print('\033[1:32mEmpréstimo Autorizado!\033[m')
    print('Sua prestação será de \033[1:32mR$ {:.2f}\033[m mensais durante \033[1:33m{}\033[m meses!'.format(prestacao_mensal,parcelas))
else:
    print('\033[1:32mEmpréstimo Não Autorizado!\033[m')
print('O \033[1:35mBanco S.A\033[m agradece seu contato... \033[1:32mVolte sempre!\033[m')

input('\n\033[1:34mDigite "sair" para sair: \033[m')