#=================== Inicialização ===============
import pygame
import random
import os
pygame.init()
# Criando guia princípal e nome do jogo
tamanho = 10 
largura = 480
altura = 320

janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake Retrô')

# Criando guia princípal e nome do jogo
janela = pygame.display.set_mode((480,320))
pygame.display.set_caption('Snake Retrô')
# musicas e imagens 
musica_inicio =os.path.join('assets','musicas','musica_inicio.mp3') 
pygame.mixer.music.load(musica_inicio)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
fundo_jogo = pygame.image.load('assets/Imagens/Fundo.jpeg').convert()

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    janela.fill((0,0,0))
    janela.blit(fundo_jogo, (0, 0))
    pygame.display.update()

pygame.quit()