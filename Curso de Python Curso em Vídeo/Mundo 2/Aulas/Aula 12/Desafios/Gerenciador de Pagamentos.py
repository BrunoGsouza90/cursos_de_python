import time

print('\n\033[1:31:40m{:=^20}\033[m'.format('Lojas HP'))
valor = float(input('\nDigite o valor do produto: \033[32mR$\033[m '))
print('''
Para pagar à vista em \033[34mDinheiro / Cheque\033[m com \033[33m10%\033[m de desconto... \033[1:31mDigite \033[m\033[4:31m1\033[m!
Para pagar à vista no \033[34mCartão\033[m com \033[33m5%\033[m de desconto... \033[1:31mDigite \033[4:31m2\033[m!\033[m
Para pagar em até \033[34m2x no cartão\033[m sendo seu \033[33mpreço normal\033[m... \033[1:31mDigite \033[4:31m3\033[m!\033[m
Para pagar em \033[34m 3x ou mais\033[m no cartão com \033[33m20% de juros\033[m... \033[1:31mDigite \033[4:31m4\033[m!\033[m''')
condicao = int(input('\nDigite a condição de pagamento: '))
print('\n\033[1:35mPROCESSANDO...\033[m')
time.sleep(2)
if condicao == 1:
    print('\nO valor a ser pago é de: \033[1:31mR$ {:.2f}\033[m!'.format(valor - (valor * 10 / 100)))
elif condicao == 2:
    print('\nO valor a ser pago é de: \033[1:31mR$ {:.2f}\033[m!'.format(valor - (valor * 5 / 100)))
elif condicao == 3:
    print('\nO valor a ser pago é de: \033[1:31mR$ {:.2f}\033[m!'.format(valor))
elif condicao == 4:
    print('\nO valor a ser pago é de: \033[1:31mR$ {:.2f}\033[m!'.format(valor + (valor * 20 / 100)))
else:
    print('\n\033[1:31mOpção Inválida!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')