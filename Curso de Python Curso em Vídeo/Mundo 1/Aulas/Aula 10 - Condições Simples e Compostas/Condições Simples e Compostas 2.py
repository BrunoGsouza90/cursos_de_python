import emoji,pygame

pygame.init()
pygame.mixer_music.load('É tudo sobre você.mp3')
pygame.mixer_music.play()
pygame.event.wait()

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi {:.1f}!'.format(media))
if media >= 7:
    print('Você está aprovado!')
else:
    print('Você reprovou!')
print('Parabéns ' + emoji.emojize('\U0001f913',language='pt') if media >= 7 else 'Estude mais ' + emoji.emojize('\U0001f4d6',language='pt'))
input('Digite "sair" para sair: ')