#=================== Inicialização ===============
import pygame
import random
import os
from Classes import *

pygame.init()

# Definindo medidas
tamanho = 10 
largura = 480
altura = 320

# Definindo cores
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)
preto = (0, 0, 0)


janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake Retrô')

# Criando guia princípal e nome do jogo
janela = pygame.display.set_mode((480,320))
pygame.display.set_caption('Snake Retrô')

# Musicas e imagens 
musica_inicio =os.path.join('assets','musicas','musica_inicio.mp3') 
pygame.mixer.music.load(musica_inicio)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
fundo_jogo = pygame.image.load('assets/Imagens/Fundo.jpeg').convert()

#maça aparecendo em lugar aleatorio 
maca_w= 15
maca_h= 15
maca= pygame.image.load('assets/Imagens/Untitled-1.png').convert()
maca_pequena=pygame.transform.scale(maca, (maca_w, maca_h))
maca_x = random.randint(0,480)
maca_y = random.randint(0,320)

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    janela.fill((0,0,0))
    janela.blit(fundo_jogo, (0, 0))
    janela.blit(maca_pequena, (maca_x, maca_y))
    pygame.display.update()

pygame.quit()