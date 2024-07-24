import pygame
from pygame.locals import * 
from sys import exit 
from random import randint 

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_fundo = pygame.mixer.music.load('smw_game_over.wav')  
pygame.mixer.music.play(-1) 

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')  

largura_tela = 640 
altura_tela = 480
largura_objeto = 20
altura_objeto = largura_objeto
 
x_cobra = largura_tela/2 - largura_objeto/2
y_cobra = altura_tela/2 - altura_objeto/2

velocidade = 10 
x_controle = velocidade 
y_controle = 0    

x_maca = randint(40, 600)
y_maca = randint(50, 430)

fonte = pygame.font.SysFont('arial', 40, True, False) #parametros para fonte, tamanho, se quer negrito e se quer italico

pontos = 0



tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Joguinho')
relogio = pygame.time.Clock()

lista_cobra = [] 
comprimento_inicial = 5  

morreu = False


def aumenta_cobra(lista_cobra): 
    for XeY in lista_cobra: 
        #XeY = [x,y]
        #lista_cobra é uma lista com varias listas no formato [x,y] dentro 
        pygame.draw.rect(tela,  (29,33,32), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo(): 
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura_tela/2 - largura_objeto/2
    y_cobra = altura_tela/2 - altura_objeto/2
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False
  
      

while True: 
    relogio.tick(10) #numero de frames p/s do jogo 
    tela.fill((75,95,88))


    mensagem = f'Pontos: {pontos}'
    texto_formatado =  fonte.render(mensagem, True, (29,33,32)) #paramentros para string, serrilhamento e cor


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            exit()
            
        if event.type == KEYDOWN: 
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0 
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass  
                else:
                    x_controle = velocidade
                    y_controle = 0  
            if event.key == K_w: 
                if y_controle == velocidade: 
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0 
            if event.key == K_s: 
                if y_controle == -velocidade:
                    pass
                else: 
                    y_controle = velocidade
                    x_controle = 0  
    '''
    if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra - 20
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 20 
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 20 
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 20 
        '''
 
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle


    cobra = pygame.draw.rect(tela, (29,33,32), (x_cobra,y_cobra,largura_objeto,altura_objeto))
    maca = pygame.draw.rect(tela, (70,33,32), (x_maca,y_maca,20 ,20))
 
  
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1     

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)



    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1: 
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = f'Game Over! Pressione a tecla R para jogar novamente.'
        texto_formatado = fonte2.render(mensagem, True, (29,33,32))
        ret_texto = texto_formatado.get_rect()

        morreu = True 
        while morreu: 
            tela.fill((75,95,88))
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    pygame.quit() 
                    exit()
                if event.type == KEYDOWN:   
                     if event.key == K_r: 
                         reiniciar_jogo()
            
            ret_texto.center = (largura_tela//2, altura_tela//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()  

    if x_cobra > largura_tela: 
         x_cobra = 0 
    if x_cobra < 0: 
        x_cobra = largura_tela
    if y_cobra < 0: 
        y_cobra = altura_tela
    if y_cobra > altura_tela: 
        y_cobra = 0 

                            

    if len(lista_cobra) > comprimento_inicial: 
         del lista_cobra[0]

    aumenta_cobra(lista_cobra) 
 

   
   

    tela.blit(texto_formatado, (430, 40))
    pygame.display.update() 