import pygame
import random

tamanho = 10 
largura = 480
altura = 320

verde_escuro = (0,128,0)

tela = pygame.display.set_mode((largura, altura))

class Cobra:
    def __init__(self):
        self.x = random.randint(0,largura - tamanho)
        self.y = random.randint(0, altura - tamanho)
        self.vel_y = 10
        self.vel_x = 10
        self.x_ctrl = 10
        self.y_ctrl = 0
        self.compr_inicial = 1
        self.lis_cobra = []
        self.lis_cbc = []


    def imagem(self):
        self.img = pygame.draw.rect(tela, verde_escuro, (self.x, self.y, tamanho, tamanho) )

# movimentos da cobra
    def movimentacao (self,deltax,deltaxelse,deltayelse):
        if self.x_ctrl == deltax:
            pass
        else:
            self.x_ctrl = deltaxelse
            self.y_ctrl = deltayelse

    def mov(self):
        self.x += self.x_ctrl
        self.y += self.y_ctrl
        if self.y < 0:
            self.y = altura - 10
        if self.x < 0:
            self.x = largura - 10
        if self.y > altura - 10:
            self.y = 0
        if self.x > largura - 10:
            self.x = 0
        
    def comp_inicial(self):
        self.compr_inicial += 1
    
    #aumento do tamanho da cobra
    def comprimento(self, lis_cobra):
        for XeY in lis_cobra:
            pygame.draw.rect(tela, verde_escuro, (XeY[0], XeY[1], tamanho, tamanho))

    def cabeca(self):
        self.lis_cbc.append(self.x)
        self.lis_cbc.append(self.y)
        self.lis_cobra.append(self.lis_cbc)

