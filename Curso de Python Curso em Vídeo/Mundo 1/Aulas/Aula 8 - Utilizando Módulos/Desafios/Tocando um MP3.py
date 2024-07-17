import pygame
pygame.init()
pygame.mixer_music.load('Tocando um MP3.mp3')
pygame.mixer_music.play()
pygame.event.wait()
input('Digite "sair" para sair: ')