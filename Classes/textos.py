from pygame.constants import JOYHATMOTION
import pygame
largura = 480
altura = 320

janela = pygame.display.set_mode((largura,altura))
class textos:
    def __init__(self, msg, cor, tam):
            self.font = pygame.font.SysFont(None, tam)
            self.texto = self.font.render(msg, True, cor)

    def mostra(self, x, y):
            janela.blit(self.texto, [x, y])

