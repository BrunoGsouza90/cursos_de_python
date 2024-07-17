import random
print('\n\033[4:31mComputador\033[m\033[1:31m -\033[m\033[1:32m Consegue adivinhar qual número eu escolhi de 1 á 10?\033[m')
computador = random.randint(1,10)
acertou = False
while not acertou:
    palpite = int(input('\n\033[1:34mDigite seu palpite:\033[m '))
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('\033[1:32mMais... Tente mais uma vez!\033[m')
        else:
            print('\033[1:32mMenos... Tente mais uma vez!\033[m')
print('\n','\033[1:31m=-\033[m' * 13)
print(' \033[1:32mParabéns... Você Acertou!\033[m')
print('','\033[1:31m=-\033[m' * 13)