import random
import time

lista = []
jogos = int(input('\n\033[1:34mDigite a quantidade de jogos que serão gerados: \033[m'))
for c in range(jogos):
    lista.append(random.sample(range(1, 60), 6))
print('\n' + '\033[1:31:40m-=\033[m' * 4 + '\033[1:32:40mSORTEANDO OS JOGOS\033[m' + '\033[1:31:40m-=\033[m' * 4)
for x,c in enumerate(lista):
    print(f'\033[4:31:40mJogo {x + 1}\033[m\033[31:40m -\033[m\033[1:33:40m {sorted(c)}\033[m')
    time.sleep(1)
print('\033[1:31:40m-=\033[m' * 17)
input('\n\033[1:34mDigite "sair" para sair: \033[m')