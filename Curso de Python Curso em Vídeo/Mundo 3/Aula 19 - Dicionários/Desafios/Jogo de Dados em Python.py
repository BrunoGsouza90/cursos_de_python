import random
import time

numeros = random.sample(range(1,7),4)
dicionario = {
    'Jogador 1':numeros[0],
    'Jogador 2':numeros[1],
    'Jogador 3':numeros[2],
    'Jogador 4':numeros[3],
}
print('')
for k,v in dicionario.items():
    print(f'\033[1:31mO\033[m \033[1:33m{k}\033[m \033[1:31mtirou\033[m \033[1:33m{v}\033[m \033[1:31m!\033[m')
    time.sleep(1)
print('\n\033[1:35mRanking dos Jogadores:\033[m\n')
for y,(k,v) in enumerate(sorted(dicionario.items(), key=lambda item: item[1])):
    print(f'\033[1:31m{y + 1}º Lugar:\033[m \033[1:33m{k}\033[m \033[1:31mcom\033[m \033[1:33m{v}\033[m \033[1:31m!\033[m')
    time.sleep(1)
input('\n\033[1:34mDigite "sair" para sair: \033[m')