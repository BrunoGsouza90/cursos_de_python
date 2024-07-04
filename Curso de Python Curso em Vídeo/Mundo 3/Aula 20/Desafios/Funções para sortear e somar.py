import random,time
def sorteia(lista):
    print('\n\033[1:35mOs números sorteados foram:')
    for num in lista:
        print(f'\033[1:31m{num}', end='\033[1:31m,\033[m ', flush=True)
        time.sleep(0.5)
    print('\033[1:33mFim!\033[m')
def somaPar(lista):
    pares = 0
    for num in lista:
        if num % 2 == 0:
            pares += num
    print(f'\033[1:31mA lista é\033[m \033[1:33m{lista}\033[m\033[1:31m. E valores pares nela são\033[m \033[1:33m{pares}\033[m\033[1:31m:\033[m')

lista = random.sample(range(1, 20), 5)
sorteia(lista)
somaPar(lista)

input('\n\033[1:34mDigite "sair" para sair: \033[m')