#=================== Inicialização ===============
#from Classes.maca import macav
from Classes.Cobra import Cobra
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
cinzaClaro=(220,220,220)

# Criando guia princípal e nome do jogo
fps = pygame.time.Clock()
janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake Retrô')



# Musicas e imagens 
musica_inicio =os.path.join('assets','musicas','musica_inicial.mp3')
musica_final=os.path.join('assets','musicas', 'musica_fim.mp3') 
pygame.mixer.music.load(musica_inicio)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
fundo_jogo = pygame.image.load('assets/Imagens/Fundo.jpeg').convert()


#maça aparecendo em lugar aleatorio 
maca_w= 15
maca_h= 15

maca= pygame.image.load('assets/Imagens/Untitled-1.png').convert()
maca_pequena =pygame.transform.scale(maca, (maca_w, maca_h))
maca_x = random.randint(0,480)
maca_y = random.randint(0,320)


class textos:
    def __init__(self, msg, cor, tam):
            self.font = pygame.font.SysFont(None, tam)
            self.texto = self.font.render(msg, True, cor)

    def mostra(self, x, y):
            janela.blit(self.texto, [x, y])



game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    janela.fill((0,0,0))
    janela.blit(fundo_jogo, (0, 0))
    janela.blit(maca_pequena, (maca_x, maca_y))
    pygame.display.update()


# encerramento do jogo
jogo = False
fim_do_jogo = False
inicio_do_jogo = True

cob = Cobra()
#mac = maca()
palavra = textos("Game Over", vermelho, 37)
palavra2 = textos("Pontuação: " , branco, 27)
palavra3 = textos("aperte Q",branco,27)
palavra4 = textos("Deseja continuar?",branco,27)
palavra5 = textos("Snake Retrô",branco,35)
palavra6 = textos("Escolha o nível de dificuldade do jogo",vermelho,27)


while inicio_do_jogo:
    janela.blit(fundo_jogo,(0,0)) 
    palavra5.mostra(0,0)
    palavra6.mostra(80,30)
    
    # escolha da dificuldade 
    pygame.draw.rect(janela, cinzaClaro, [43, 118, 139, 31])
    pygame.draw.rect(janela, preto, [45, 120, 135, 27])
    facil = textos("fácil(1)", branco, 30)
    facil.mostra(80, 125)

    pygame.draw.rect(janela, cinzaClaro, [43, 168, 139, 31])
    pygame.draw.rect(janela, preto, [45, 170, 135, 27])
    medio = textos("médio(2)", branco, 30)
    medio.mostra(73, 175)

    pygame.draw.rect(janela, cinzaClaro, [43, 218, 139, 31])
    pygame.draw.rect(janela, preto, [45, 220, 135, 27])
    dificil = textos("díficil(3)", vermelho, 30)
    dificil.mostra(74, 225)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicio_do_jogo=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                fps.tick(10)
                jogo=True
            elif event.key == pygame.K_2:
                fps.tick(20)
                jogo=True
            elif event.key == pygame.K_3:
                fps.tick(35)
                jogo=True    
    # while do jogo em si

        while fim_do_jogo:
            janela.fill(preto)
            palavra.mostra(95,130)
            palavra3.mostra(175,210)
            palavra4.mostra(5,210)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogo = False
                    fim_do_jogo = False
                    inicio_do_jogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_do_jogo=False
                        jogo=True
                        cob.recomeco()
                        #falta atualizar os pontos
                        pygame.mixer.music.load(musica_inicio)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
        if fim_do_jogo == True:
        # musica do final 
            pygame.mixer.music.pause()
            pygame.mixer.music.load(musica_final)
            pygame.mixer.music.set_volume(0.5) 
            pygame.mixer.music.play(1)        

    pygame.display.update()



pygame.quit()