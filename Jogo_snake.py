#=================== Inicialização ===============
import pygame
import random
import os

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
cinzaClaro = (220,220,220)

# Criando guia princípal e nome do jogo
clock = pygame.time.Clock()
fps = 15
janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake Retrô')

# Musicas e imagens 
musica_inicio =os.path.join('assets','musicas','musica_inicial.mp3')
musica_final=os.path.join('assets','musicas', 'musica_fim.mp3') 
pygame.mixer.music.load(musica_inicio)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
fundo_jogo = pygame.image.load('assets/Imagens/Fundo.jpeg').convert()
menu = pygame.image.load('assets/Imagens/Untitled.jpg').convert()

jogo = False
fim_do_jogo = False
inicio_do_jogo = True

class textos:
    def __init__(self, msg, cor, tam):
            self.font = pygame.font.SysFont(None, tam)
            self.texto = self.font.render(msg, True, cor)
    def mostra(self, x, y):
            janela.blit(self.texto, [x, y])

palavra = textos("Game Over", vermelho, 80)
palavra2 = textos("Pontuação: " , branco, 27)
palavra3 = textos("Aperte Espaço", branco,27)
palavra4 = textos("Deseja continuar?", branco,27)
palavra5 = textos("Snake Retrô", branco,35)
palavra6 = textos("Escolha o nível de dificuldade do jogo:", vermelho,27)


all_sprites = pygame.sprite.Group()
cobra = Cobra()
all_sprites.add(cobra)

estado = 'inicio'
#========Menu==============
while inicio_do_jogo:
    clock.tick(fps)
    if estado == 'inicio':

        janela.blit(menu,(0,0)) 
        # escolha da dificuldade 
        pygame.draw.rect(janela, cinzaClaro, [23, 160, 139, 31])
        pygame.draw.rect(janela, preto, [25, 162, 135, 27])
        facil = textos("Fácil(1)", branco, 30)
        facil.mostra(60, 166)

        pygame.draw.rect(janela, cinzaClaro, [173, 160, 139, 31])
        pygame.draw.rect(janela, preto, [175, 162, 135, 27])
        medio = textos("Médio(2)", branco, 30)
        medio.mostra(199, 166)

        pygame.draw.rect(janela, cinzaClaro, [323, 160, 139, 31])
        pygame.draw.rect(janela, preto, [325, 162, 135, 27])
        dificil = textos("Díficil(3)", vermelho, 30)
        dificil.mostra(353, 166)
        pygame.display.update()
        #Escolha da dificuldade do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inicio_do_jogo=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    fps = 10
                    jogo = True
                elif event.key == pygame.K_2:
                    fps = 15
                    jogo = True
                elif event.key == pygame.K_3:
                    fps = 35
                    jogo = True       
    else:
        # loop principal
        contador = 0
        while jogo:
            janela.blit(fundo_jogo,(0,0)) 
            palavra2.mostra(340, 0)
            contador = str(contador)
            cont = textos(contador,branco,27)
            cont.mostra(445,0)

pygame.quit()