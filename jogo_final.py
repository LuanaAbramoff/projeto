import pygame
import random
import os
from Objetos import Bombinha, Maca_dourada, Maca, Textos, Cobra

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

#criando a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Retrô')

# Musicas e imagens
fundo_jogo = pygame.image.load("assets/Imagens/Fundo.jpeg").convert()
musica_inicio =os.path.join('assets','musicas','musica_inicial.mp3')
musica_final=os.path.join('assets','musicas', 'musica_fim.mp3') 
menu = pygame.image.load('assets/Imagens/Untitled.jpg').convert()
mus_pontuacao = os.path.join('assets','musicas','pontuação.wav')

#criando o clock e definindo FPS
clock = pygame.time.Clock()
fps = 15

# defenindo palavras 
palavra = Textos.Textos("Game Over", vermelho, 90)
palavra2 = Textos.Textos("Pontuação: " , branco, 40)
palavra3 = Textos.Textos("Aperte Espaço", branco, 32)
palavra4 = Textos.Textos("Deseja continuar?", branco,32)
palavra5 = Textos.Textos("Snake Retrô", branco,27)
palavra6 = Textos.Textos("Escolha o nível de dificuldade do jogo:", vermelho,27)
palavra7 = Textos.Textos('Record: ', branco, 38)
record = 0


# loop do jogo
sair = False
while not sair:
    pygame.mixer.music.load(musica_inicio)
    pygame.mixer.music.set_volume(0.5)    
    pygame.mixer.music.play(-1)
    inicio_do_jogo = True
    while inicio_do_jogo:
        tela.blit(menu,(0,0)) 
        #Tela inicial/ menu do jogo
        pygame.draw.rect(tela, cinzaClaro, [23, 160, 139, 31])
        pygame.draw.rect(tela, preto, [25, 162, 135, 27])
        facil = Textos.Textos("Fácil(1)", branco, 30)
        facil.mostra(60, 166)

        pygame.draw.rect(tela, cinzaClaro, [173, 160, 139, 31])
        pygame.draw.rect(tela, preto, [175, 162, 135, 27])
        medio = Textos.Textos("Médio(2)", branco, 30)
        medio.mostra(199, 166)

        pygame.draw.rect(tela, cinzaClaro, [323, 160, 139, 31])
        pygame.draw.rect(tela, preto, [325, 162, 135, 27])
        dificil = Textos.Textos("Díficil(3)", vermelho, 30)
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

# defenindo variaveis 
    palavra2 = Textos.Textos("Pontuação: " , branco, 27)
    cobra = Cobra.Cobra()
    apple = Maca.Maca()
    goldapple= Maca_dourada.Maca_dourada()
    bomber = Bombinha.Bombinha()
    contador = 0
    morte = False
    numero_maca_dourada = 0
    numero_bomba = 0
    goldapple.convercao
    gold_maca = tela.blit(goldapple.convercao,(600,600))
# loop da jogabilidade 
    while game:
        clock.tick(fps)
        tela.fill(preto)
        tela.blit(fundo_jogo, (0,0))

        # Mostra pontuação do jogo
        palavra2.mostra(340,0)
        cont = Textos.Textos(str(contador), branco, 27)
        cont.mostra(445,0)

        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
                sair = True

            if event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    cobra.movimentacao(10,-10,0)
                    
                if event.key == K_d or event.key == K_RIGHT:
                    cobra.movimentacao(-10,10,0)

                if event.key == K_s or event.key == K_DOWN:
                    cobra.movimentacao(10,0,-10)

                if event.key == K_w or event.key == K_UP:
                    cobra.movimentacao(-10,0,10)

        cobra.mov()

        cobra.imagem()
        apple.convercao
        maca = tela.blit(apple.convercao, (apple.pos_x,apple.pos_y))
        cobrinha = cobra.img
        
        if contador > record:
            record = contador
        # colisao maca + cobra
        if cobrinha.colliderect(maca):
            #Gerando nova maca
            apple.convercao
            apple.pos_x = random.randint(0,(largura-tamanho)/10)*10
            apple.pos_y = random.randint(0,(altura-tamanho)/10)*10
            tela.blit(apple.convercao, (apple.pos_x,apple.pos_y))
            contador += 1
            numero_maca_dourada = random.randint(0,10)
            numero_bomba = random.randint(0,8)
            mus = pygame.mixer.Sound(mus_pontuacao)
            pygame.mixer.music.set_volume(0.5)
            mus.play()

            #Alterando Cobra
            cobra.cabeca()
            cobra.comprimento(cobra.lis_cobra)
            cobra.comp_inicial()

        # maca dourada 
        if numero_maca_dourada == 10:
            goldapple.convercao
            gold_maca=tela.blit(goldapple.convercao,(goldapple.pos2_x,goldapple.pos2_y))
            if cobrinha.colliderect(gold_maca):
                goldapple.convercao
                goldapple.pos2_x = random.randint(0,(largura-tamanho)/10)*10
                goldapple.pos2_y = random.randint(0,(altura-tamanho)/10)*10
                contador += 10
                numero_maca_dourada = random.randint(0,10)
                mus = pygame.mixer.Sound(mus_pontuacao)
                pygame.mixer.music.set_volume(0.5)
                mus.play()

                cobra.cabeca()
                cobra.comprimento(cobra.lis_cobra)
                cobra.comp_inicial()

        # bomba 
        if numero_bomba == 5:
            bomber.convercao
            bomba = tela.blit(bomber.convercao, (bomber.pos4_x,bomber.pos4_y))
            if cobrinha.colliderect(bomba):
                game = False
                morte = True

        cobra.lis_cbc = []
        cobra.cabeca()

        #morte da cobra
        if cobra.lis_cobra.count(cobra.lis_cbc) > 1:
            game = False
            morte = True
            
        #corpo da cobra
        if len(cobra.lis_cobra) > cobra.compr_inicial:
            del cobra.lis_cobra[0]
            
        cobra.comprimento(cobra.lis_cobra)
        
        pygame.display.update()
    # musica do final 
    pygame.mixer.music.pause()
    pygame.mixer.music.load(musica_final)
    pygame.mixer.music.set_volume(0.5) 
    pygame.mixer.music.play(1)
    # loop da morte 
    while morte:
        tela.fill(preto)
        palavra.mostra(70,5)
        palavra2.mostra(150,100)  #pontuação
        cont.mostra(255,100)
        palavra3.mostra(280,260)
        palavra4.mostra(80,260)
        palavra7.mostra(150, 180)
        recorde = Textos.Textos(str(record), branco, 35)
        recorde.mostra(255, 180)

        # reinicio do jogo caso o jogador queira 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                morte = False
                sair = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    morte = False
                    game = True
                    pygame.mixer.music.pause()

        pygame.display.update()
# sair do jogo 
pygame.quit()