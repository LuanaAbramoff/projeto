import pygame

largura = 480
altura = 320

tela = pygame.display.set_mode((largura, altura))

class Textos:
    def __init__(self, msg, cor, tam):
            self.font = pygame.font.SysFont(None, tam)
            self.texto = self.font.render(msg, True, cor)
    def mostra(self, x, y):
            tela.blit(self.texto, [x, y])