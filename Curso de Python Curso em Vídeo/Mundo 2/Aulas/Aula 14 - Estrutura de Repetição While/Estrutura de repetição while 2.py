print('')
n = 1
while n != 0:
    n = int(input('\033[1:33mDigite um valor: \033[m'))
print('\n\033[1:31:40mFim\033[m\n')

resposta = 'Sim'
while resposta == 'Sim':
    resposta = str(input('\033[1:33mQuer continuar? \033[m')).upper().strip()
print('\n\033[1:31:40mFim\033[m\n')

input('\n\033[1:34mDigite "sair" para sair: \033[m')
23