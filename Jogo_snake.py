#=================== Inicialização ===============
import pygame
import random

pygame.init()

# Criando guia princípal e nome do jogo
janela = pygame.display.set_mode((480,320))
pygame.display.set_caption('Snake Retrô')

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