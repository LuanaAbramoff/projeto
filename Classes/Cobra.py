from random import *
import pygame
class Cobra:
    def __init__(self):
        self.x = randint(0,(largura-tamanho)/10)*10
        self.y = randint(0,(altura-tamanho)/10)*10
        self.velocidade_em_x = 0
        self.velocidade_em_y = 0
        self.cobra_xy = []
        self.cobra_comprimento = 1
        self.cobra_inicial = []
        self.pontuacao = 0
        self.fimdejogo = False
    def movimentos_possiveis(self):
        self.cobra_0 = [self.x,self.y]
        self.cobra_xy.append(self.cobra_inicial) 
    def crescimento_cobra(self):
        self.cobra_comprimento += 1
    def imagem_cobra(self):
        for XY in self.cobra_xy:
            pygame.draw.rect(fundo_jogo,branco,[XY[0],XY[1],tamanho,tamanho])
    def resto(self):
        if len(self.cobra_xy) > self.cobra_comp:
            del self.cobra_xy[0]
    def morte(self):
        if any(Bloco == self.cobra_0 for Bloco in self.cobra_xy[:-1]):
            self.fimdejogo = True