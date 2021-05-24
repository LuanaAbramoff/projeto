#=================== Inicialização ===============
import pygame
import random
import os
pygame.init()
# Criando guia princípal e nome do jogo
janela = pygame.display.set_mode((480,320))
pygame.display.set_caption('Snake Retrô')

tamanho = 10 
largura=480
altura=320

plano_fundo = pygame.image.load('img/img123.jpg').convert() 
plano_fundo = pygame.transform.scale(plano_fundo,(largura,altura)) 

# Criando guia princípal e nome do jogo
janela = pygame.display.set_mode((480,320))
pygame.display.set_caption('Snake Retrô')

fundo_jogo = pygame.image.load('assets/Fundo.jpeg').convert()

game= True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    janela.fill((0,0,0))
    janela.blit(fundo_jogo, (0, 0))
    pygame.display.update()

pygame.quit()