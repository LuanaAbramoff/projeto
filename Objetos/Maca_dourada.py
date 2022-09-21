import pygame
import random

# Definindo medidas
tamanho = 10 
largura = 480
altura = 320

class Maca_dourada:
    def __init__(self):
        self.pos2_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos2_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 14
        self.h = 14
        self.img = pygame.image.load('assets/Imagens/Golden_Apple_JE2_BE2.png').convert_alpha()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))
