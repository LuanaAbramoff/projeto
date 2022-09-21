import pygame
import random

tamanho = 10 
largura = 480
altura = 320

class Bombinha:
    def __init__(self):
        self.pos4_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos4_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 20
        self.h = 20
        self.img = pygame.image.load('assets/Imagens/bombinha.png').convert_alpha()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))