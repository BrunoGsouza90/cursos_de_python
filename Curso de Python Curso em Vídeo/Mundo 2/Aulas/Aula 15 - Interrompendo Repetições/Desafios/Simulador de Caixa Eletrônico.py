import time

escolha = saldo = sacar = cem = cinquenta = vinte = dez = um = valor = parcelas = salario = prestacao_mensal = continuar = 0
print('\n   \033[1:35:40mBem vindo ao Banco J.A\033[m')
while True:
    escolha = int(input('''
\n\033[1:34mQual opção você deseja realizar?\033[m
\033[1:31m[1]\033[m \033[1:33mSacar\033[m
\033[1:31m[2]\033[m \033[1:33mDepositar\033[m
\033[1:31m[3]\033[m \033[1:33mEmpréstimo\033[m
\033[1:34mDigite aqui:\033[m '''))
    while escolha not in (1,2,3):
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        escolha = int(input('''
\033[1:34mQual opção você deseja realizar?\033[m
\033[1:31m[1]\033[m \033[1:33mSacar\033[m
\033[1:31m[2]\033[m \033[1:33mDepositar\033[m
\033[1:31m[3]\033[m \033[1:33mEmpréstimo\033[m
\033[1:34mDigite aqui:\033[m '''))
    if escolha == 1:
        sacar = int(input('\n\033[1:34mQuanto você deseja sacar?\033[m '))
        if saldo - sacar > -250:
            saldo -= sacar
            cem = sacar // 100
            sacar %= 100
            cinquenta = sacar // 50
            sacar %= 50
            vinte = sacar // 20
            sacar %= 20
            dez = sacar // 10
            sacar %= 10
            cinco = sacar // 5
            sacar %= 5
            dois = sacar // 2
            sacar %= 2
            um = sacar // 1
            print(f'''
\033[1:31:40mCédulas:\033[m

\033[1:31m{cem}\033[m = \033[1:33mNotas de Cem Reais\033[m \033[1:32m(R$ 100,00)\033[m
\033[1:31m{cinquenta}\033[m = \033[1:33mNotas de Cinquenta Reais\033[m \033[1:32m(R$ 50,00)\033[m
\033[1:31m{vinte}\033[m = \033[1:33mNotas de Vinte Reais\033[m \033[1:32m(R$ 20,00)\033[m
\033[1:31m{dez}\033[m = \033[1:33mNotas de Dez Reais\033[m \033[1:32m( R$ 10,00 )\033[m
\033[1:31m{cinco}\033[m = \033[1:33mNotas de Cinco Reais\033[m \033[1:32m(R$ 5,00)\033[m
\033[1:31m{dois}\033[m = \033[1:33mNotas de Dois Reais\033[m \033[1:32m( R$ 2,00 )\033[m
\033[1:31m{um}\033[m = \033[1:33mMoedas de Um Real\033[m \033[1:32m( R$ 1,00 )\033[m
\033[1:31mTotal =\033[m \033[1:32mR$ {cem * 100 + cinquenta * 50 + vinte * 20 + dez * 10 + cinco * 5 + dois * 2 + um },00\033[m ''')
            print(f'\033[1:31mSeu Saldo atual é de\033[m \033[1:32mR$ {saldo:.2f}\033[m\033[1:31m!\033[m')
        else:
            print('\n\033[1:31mSaldo Insuficiente!\033[m')
    elif escolha == 2:
        sacar = float(input('\n\033[1:34mQuanto você deseja depositar?\033[m '))
        saldo += sacar
        print(f'\033[1:31mSeu Saldo atual é de\033[m \033[1:32mR$ {saldo:.2f}\033[m\033[1:31m!\033[m')
    elif escolha == 3:
        valor = float(input('\n\033[1:34mDigite o valor da casa que deseja fazer o empréstimo:\033[m \033[32mR$ \033[m'))
        salario = float(input('\033[1:34mDigite o seu salário:\033[m \033[32mR$ \033[m'))
        parcelas = int(input('\033[1:34mDigite em quantas vezes você vai pagar:\033[m '))
        print('\033[1:35m\nPROCESSANDO...\033[m\n')
        time.sleep(2)
        if valor / parcelas <= salario * 30 / 100:
            prestacao_mensal = valor / parcelas
            print('\033[1:32mEmpréstimo Autorizado!\033[m')
            print('\033[1:31mSua prestação será de\033[m \033[1:32mR$ {:.2f}\033[m \033[1:31mmensais durante\033[m\033[1:33m{}\033[m \033[1:31mmeses!\033[m'.format(prestacao_mensal, parcelas))
        else:
            print('\033[1:32mEmpréstimo Não Autorizado!\033[m')
    continuar = str(input('\n\033[1:34mQuer fazer outra operação?\033[m \033[1:35m[S/N]\033[m ')).strip().title()
    while continuar not in 'SsNn':
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        continuar = str(input('\n\033[1:34mQuer fazer outra operação?\033[m \033[1:35m[S/N]\033[m ')).strip().title()
    if continuar in 'Nn':
        break
input('\n\033[1:34mDigite "sair" para sair: \033[m')