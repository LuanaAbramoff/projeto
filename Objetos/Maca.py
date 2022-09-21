import pygame
import random

tamanho = 10
largura = 480
altura = 320

class Maca:
    def __init__(self):
        self.pos_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 14
        self.h = 14
        self.img = pygame.image.load('assets/Imagens/maca_mine.png').convert_alpha()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))