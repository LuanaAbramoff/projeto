import pygame
import random
import os

from pygame.constants import KEYDOWN, K_BACKSPACE, K_DOWN, K_LEFT, K_RIGHT, K_UP, K_a, K_d, K_r, K_s, K_w, QUIT

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
verde_escuro = (0,128,0)




tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Retrô')


# Musicas e imagens
fundo_jogo = pygame.image.load("assets/Imagens/Fundo.jpeg").convert()
musica_inicio =os.path.join('assets','musicas','musica_inicial.mp3')
musica_final=os.path.join('assets','musicas', 'musica_fim.mp3') 
# pygame.mixer.music.load(musica_inicio)
# pygame.mixer.music.set_volume(0.4)    
# pygame.mixer.music.play(-1)
menu = pygame.image.load('assets/Imagens/Untitled.jpg').convert()
mus_pontuacao = os.path.join('assets','musicas','pontuação.wav')

clock = pygame.time.Clock()
fps = 15



def comprimento(lis_cobra):
    for XeY in lis_cobra:
        pygame.draw.rect(tela, verde_escuro, (XeY[0], XeY[1], tamanho, tamanho))

class Maca:
    def __init__(self):
        self.pos_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 14
        self.h = 14
        self.img = pygame.image.load('assets/Imagens/maca_mine.png').convert_alpha()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))
        
class Maca_dourada:
    def __init__(self):
        self.pos2_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos2_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 14
        self.h = 14
        self.img = pygame.image.load('assets/Imagens/Golden_Apple_JE2_BE2.png').convert_alpha()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))


class Maca_azul:
    def __init__(self):
        self.pos3_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos3_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 14
        self.h = 14
        self.img = pygame.image.load('assets/Imagens/azul_mine.png').convert()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))

class Bombinha:
    def __init__(self):
        self.pos4_x = random.randint(0,(largura-tamanho)/10)*10
        self.pos4_y = random.randint(0,(altura-tamanho)/10)*10
        self.w = 20
        self.h = 20
        self.img = pygame.image.load('assets/Imagens/bombinha.png').convert_alpha()
        self.convercao = pygame.transform.scale(self.img, (self.w, self.h))

class Cobra:
    def __init__(self):
        self.x = random.randint(0,largura - tamanho)
        self.y = random.randint(0, altura - tamanho)
        self.vel_y = 10
        self.vel_x = 10
        self.x_ctrl = 10
        self.y_ctrl = 0
        self.compr_inicial = 1

    def imagem(self):
        self.img = pygame.draw.rect(tela, verde_escuro, (self.x, self.y, tamanho, tamanho) )

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
            self.y = altura - 10
        if self.x < 0:
            self.x = largura - 10
        if self.y > altura - 10:
            self.y = 0
        if self.x > largura - 10:
            self.x = 0
        
    def comp_inicial(self):
        self.compr_inicial += 1
       
class textos:
    def __init__(self, msg, cor, tam):
            self.font = pygame.font.SysFont(None, tam)
            self.texto = self.font.render(msg, True, cor)
    def mostra(self, x, y):
            tela.blit(self.texto, [x, y])

palavra = textos("Game Over", vermelho, 80)
palavra2 = textos("Pontuação: " , branco, 27)
palavra3 = textos("Aperte Espaço", branco,27)
palavra4 = textos("Deseja continuar?", branco,27)
palavra5 = textos("Snake Retrô", branco,35)
palavra6 = textos("Escolha o nível de dificuldade do jogo:", vermelho,27)

inicio_do_jogo = True
while inicio_do_jogo:
    tela.blit(menu,(0,0)) 
    # escolha da dificuldade 
    pygame.draw.rect(tela, cinzaClaro, [23, 160, 139, 31])
    pygame.draw.rect(tela, preto, [25, 162, 135, 27])
    facil = textos("Fácil(1)", branco, 30)
    facil.mostra(60, 166)

    pygame.draw.rect(tela, cinzaClaro, [173, 160, 139, 31])
    pygame.draw.rect(tela, preto, [175, 162, 135, 27])
    medio = textos("Médio(2)", branco, 30)
    medio.mostra(199, 166)

    pygame.draw.rect(tela, cinzaClaro, [323, 160, 139, 31])
    pygame.draw.rect(tela, preto, [325, 162, 135, 27])
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
                game = True
                inicio_do_jogo = False
            elif event.key == pygame.K_2:
                fps = 15
                game = True
                inicio_do_jogo = False
            elif event.key == pygame.K_3:
                fps = 30
                game = True
                inicio_do_jogo = False


palavra2 = textos("Pontuação: " , branco, 27)
lis_cobra = []
cobra = Cobra()
apple = Maca()
goldapple= Maca_dourada()
blueapple= Maca_azul()
bomber = Bombinha()
contador = 0
morte = False
numerox = 0
numeroy = 0
goldapple.convercao
gold_maca = tela.blit(goldapple.convercao, (600,600))
while game:
    clock.tick(fps)
    tela.fill(preto)
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
        numerox = random.randint(0,10)
        numeroy = random.randint(0,8)
        mus = pygame.mixer.Sound(mus_pontuacao)
        pygame.mixer.music.set_volume(0.5)
        mus.play()

        x = cobra.x
        y = cobra.y
        lis_cbc.append(x)
        lis_cbc.append(y)    
        lis_cobra.append(lis_cbc)
        comprimento(lis_cobra)
        cobra.comp_inicial()

    
    if numerox == 10:
        goldapple.convercao
        gold_maca=tela.blit(goldapple.convercao,(goldapple.pos2_x,goldapple.pos2_y))
        if cobrinha.colliderect(gold_maca):
            goldapple.convercao
            goldapple.pos2_x = random.randint(0,(largura-tamanho)/10)*10
            goldapple.pos2_y = random.randint(0,(altura-tamanho)/10)*10
            contador += 10
            numerox = 0
            mus = pygame.mixer.Sound(mus_pontuacao)
            pygame.mixer.music.set_volume(0.5)
            mus.play()

            x = cobra.x
            y = cobra.y
            lis_cbc.append(x)
            lis_cbc.append(y)    
            lis_cobra.append(lis_cbc)
            comprimento(lis_cobra)
            cobra.comp_inicial()


    if numeroy == 5:
        bomber.convercao
        bomba = tela.blit(bomber.convercao, (bomber.pos4_x,bomber.pos4_y))
        if cobrinha.colliderect(bomba):
            game = False
            morte = True

    x = cobra.x
    y = cobra.y
    lis_cbc = []
    lis_cbc.append(x)
    lis_cbc.append(y)
    lis_cobra.append(lis_cbc)

    if lis_cobra.count(lis_cbc) > 1:
        game = False
        morte = True

    
    if len(lis_cobra) > cobra.compr_inicial:
        del lis_cobra[0]
        
    comprimento(lis_cobra)
    
    pygame.display.update()

pygame.mixer.music.pause()
pygame.mixer.music.load(musica_final)
pygame.mixer.music.set_volume(0.1) 
pygame.mixer.music.play(1)
while morte:
    tela.fill(preto)
    palavra.mostra(110,0)
    palavra2.mostra(80,160) #pontuação
    cont.mostra(200,160)
    palavra3.mostra(175,210)
    palavra4.mostra(5,210)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            morte = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                morte=False
                #falta colocar o reinicio
    pygame.display.update()

pygame.quit()