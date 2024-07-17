import random,emoji,pygame
import time

pygame.init()
pygame.mixer_music.load('É tudo sobre você.mp3')
pygame.mixer_music.play()
pygame.event.wait()

num = random.randint(1,10)
escolhido = input('Digite um número: ')
print('PROCESSANDO...')
time.sleep(2)
print('O número sorteado é o {}!'.format(num))
print('Você venceu ' + emoji.emojize('\U0001f4af',language='pt') if escolhido == num else 'Você perdeu ' + emoji.emojize('\U0001f623',language='pt'))

input('Digite "sair" para sair: ')