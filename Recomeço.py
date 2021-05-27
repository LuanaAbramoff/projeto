import pygame
import random
import os

from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP, K_a, K_d, K_s, K_w, QUIT

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




tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Retrô')

# Musicas e imagens
fundo_jogo = pygame.image.load('assets/Imagens/Fundo.jpeg').convert()
# musica_inicio =os.path.join('assets','musicas','musica_inicial.mp3')
# musica_final=os.path.join('assets','musicas', 'musica_fim.mp3') 
# pygame.mixer.music.load(musica_inicio)
# pygame.mixer.music.set_volume(0.4)
# pygame.mixer.music.play(-1)
# menu = pygame.image.load('assets/Imagens/Untitled.jpg').convert()
mus_pontuacao = os.path.join('assets','musicas','pontuação.wav')

clock = pygame.time.Clock()
fps = 15

game = True

def comprimento(lis_cobra):
    for XeY in lis_cobra:
        pygame.draw.rect(tela, preto, (XeY[0], XeY[1], tamanho, tamanho))

class Maca:
    def __init__(self):
        self.pos_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 14
        self.h = 14
        self.img = pygame.image.load('assets/Imagens/maca_Mine.png').convert()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))
        


class Cobra:
    def __init__(self):
        self.x = random.randint(0,largura - tamanho)
        self.y = random.randint(0, altura - tamanho)
        self.vel_y = 10
        self.vel_x = 10
        self.x_ctrl = 10
        self.y_ctrl = 0

    def imagem(self):
        self.img = pygame.draw.rect(tela, preto, (self.x, self.y, tamanho, tamanho) )

    def movimento_a(self):
        if self.x_ctrl == 10:
            pass
        else:
            self.x_ctrl = -10
            self.y_ctrl = 0
    
    def movimento_d(self):
        if self.x_ctrl == -10:
            pass
        else:
            self.x_ctrl = 10
            self.y_ctrl = 0

    def movimento_w(self):
        if self.y_ctrl == 10:
            pass
        else:
            self.x_ctrl = 0
            self.y_ctrl = -10
        

    def movimento_s(self):
        if self.y_ctrl == -10:
            pass
        else:
            self.x_ctrl = 0
            self.y_ctrl = 10

    def mov(self):
        self.x += self.x_ctrl
        self.y += self.y_ctrl
        if self.y < 0:
            self.y = altura
        if self.x < 0:
            self.x = largura
        if self.y > altura:
            self.y = 0
        if self.x > largura:
            self.x = 0

        


        
class textos:
    def __init__(self, msg, cor, tam):
            self.font = pygame.font.SysFont(None, tam)
            self.texto = self.font.render(msg, True, cor)
    def mostra(self, x, y):
            tela.blit(self.texto, [x, y])

    
palavra2 = textos("Pontuação: " , branco, 27)
lis_cobra = []
cobra = Cobra()
apple = Maca()
contador = 0
while game:
    clock.tick(fps)
    tela.fill((0,0,255))
    tela.blit(fundo_jogo, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            game = False

        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                cobra.movimento_a()
                
            if event.key == K_d or event.key == K_RIGHT:
                cobra.movimento_d()

            if event.key == K_s or event.key == K_DOWN:
                cobra.movimento_s()

            if event.key == K_w or event.key == K_UP:
                cobra.movimento_w()

    cobra.mov()

    cobra.imagem()
    apple.convercao
    maca = tela.blit(apple.convercao, (apple.pos_x,apple.pos_y))
    cobrinha = cobra.img

    palavra2.mostra(340,0)
    cont = textos(str(contador), branco, 27)
    cont.mostra(445,0)
    if cobrinha.colliderect(maca):
        apple.convercao
        apple.pos_x = random.randint(0,(largura-tamanho)/10)*10
        apple.pos_y = random.randint(0,(altura-tamanho)/10)*10
        tela.blit(apple.convercao, (apple.pos_x,apple.pos_y))
        contador += 1
        mus = pygame.mixer.Sound(mus_pontuacao)
        pygame.mixer.music.set_volume(0.5)
        mus.play()

        x = cobra.x
        y = cobra.y
        lis_cbc = []
        lis_cbc.append(x)
        lis_cbc.append(y)    
        lis_cobra.append(lis_cbc)
        comprimento(lis_cobra)
    
    x = cobra.x
    y = cobra.y
    lis_cbc = []
    lis_cbc.append(x)
    lis_cbc.append(y)
    lis_cobra.append(lis_cbc)

    if lis_cobra.count(lis_cbc) > 1:
        game = False

    comprimento(lis_cobra)
    lis_cobra.pop(0)
    
    
    
        
        

    pygame.display.update()

pygame.quit()