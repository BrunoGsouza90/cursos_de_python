import time
def contador(inicio,fim,passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'\n\033[1:33mContando de {inicio} até {fim}, de {passo} em {passo}: \033[m')
    if inicio < fim:
        for c in range(inicio,fim + 1, passo):
            print(f'\033[1:31m{inicio}\033[m', end='\033[1:31m,\033[m ', flush=True)
            inicio += passo
            time.sleep(0.5)
        print('\033[1:35mFim\033[m')
    elif inicio > fim:
        for c in range(fim + 1, inicio, passo):
            print(f'\033[1:31m{inicio}\033[m', end='\033[1:31m,\033[m ', flush=True)
            inicio -= passo
            time.sleep(0.5)
        print('\033[1:35mFim\033[m')

contador(0, 10, 1)
contador(10, 0, 2)
print(f'\n\033[1:32mAgora é sua vez! \033[m')
inicio = int(input('\033[1:34mDigite o Inicío: \033[m'))
fim = int(input('\033[1:34mDigite o Fim: \033[m'))
passo = int(input('\033[1:34mDigite o Passo: \033[m'))
contador(inicio,fim,passo)
input('\n\033[1:34mDigite "sair" para sair: \033[m')