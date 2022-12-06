import pygame
pygame.init()

janela = pygame.display.set_mode([1280, 720])
titulo = pygame.display.set_caption('Pong')

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")

campo = pygame.image.load("assets/field.png")
win = pygame.image.load("assets/win.jpg")
lose = pygame.image.load("assets/lose.png")

player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_cima = False
player1_baixo = False



player2 = pygame.image.load("assets/player2.png")
player2_y = 310


bola = pygame.image.load("assets/ball.png")
bola_x = 617
bola_y = 337
bola_direcao = -10
bola_direcao_y = 10


def desenho():
    if score1 or score2 < 3:
        janela.blit(campo, (0, 0))
        janela.blit(player1, (50, player1_y))
        janela.blit(player2, (1150, player2_y))
        janela.blit(bola, (bola_x, bola_y))
        janela.blit(score1_img, (500, 50))
        janela.blit(score2_img, (710, 50))
        movimento_bola()
        movimento_player1()
        movimento_player2()
    elif score1 > 3:
        janela.blit(win, (0, 0))


    else:
        janela.blit(lose, (0,0))

def movimento_player1():
    global player1_y

    if player1_cima:
        player1_y -= 10
    else:
        player1_y += 0

    if player1_baixo:
        player1_y += 10
    else:
        player1_y += 0

    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 574:
        player1_y = 574


def movimento_player2():
    global player2_y
    player2_y = bola_y


def movimento_bola():
    global bola_x
    global bola_y
    global bola_direcao
    global bola_direcao_y
    global score1
    global score2
    global score2_img
    global score1_img

    bola_x += bola_direcao
    bola_y += bola_direcao_y


    if bola_x < 120:
        if player1_y < bola_y + 23:
            if player1_y + 146 > bola_y:
                bola_direcao *= -1

    if bola_x > 1100:
        if player2_y < bola_y + 23:
            if player2_y + 146 > bola_y:
                bola_direcao *= -1

    if bola_y > 685:
        bola_direcao_y *= -1
    elif bola_y <= 0:
        bola_direcao_y *= -1

    if bola_x < -50:
        bola_x = 617
        bola_y = 337
        bola_direcao_y *= -1
        bola_direcao *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) +".png")

    if bola_y > 1320:
        bola_x = 617
        bola_y = 337
        bola_direcao_y *= -1
        bola_direcao *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) +".png")

def restart():
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_cima = True
                if event.key == pygame.K_s:
                    player1_baixo = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1_cima = False
                if event.key == pygame.K_s:
                    player1_baixo = False

        desenho()
        pygame.display.update()


loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_cima = True
            if event.key == pygame.K_s:
                player1_baixo = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_cima = False
            if event.key == pygame.K_s:
                player1_baixo = False

    desenho()
    pygame.display.update()