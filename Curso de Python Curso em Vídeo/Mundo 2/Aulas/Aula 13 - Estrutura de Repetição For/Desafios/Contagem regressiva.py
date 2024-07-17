import time,pygame,emoji

print('\n\033[1:31:40mPreparados para o ano novo?\033[m\n       \033[1:31:40mVamos contar!\033[m')
contagem = 10
for c in range(0,10):
    print('\033[1:33m            {}\033[m'.format(contagem))
    time.sleep(1)
    contagem = contagem - 1
print('\033[1:32:40m{}FELIZ ANO NOVO{}\033[m'.format(emoji.emojize('\U0001f389\U0001f38a\U0001f942',language='pt'),emoji.emojize('\U0001f389\U0001f38a\U0001f942',language='pt')))
pygame.init()
pygame.mixer_music.load('Fogos de Artificio.mp3')
pygame.mixer_music.play()
pygame.event.wait
time.sleep(10)
pygame.init()
pygame.mixer_music.load('Feliz ano novo.mp3')
pygame.mixer_music.play()
pygame.event.wait
input('\n\033[1:34mDigite "sair" para sair: \033[m')