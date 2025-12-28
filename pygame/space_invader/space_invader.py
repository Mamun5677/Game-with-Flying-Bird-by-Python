import pygame
import random

# pygame initialization
pygame.init()

# window
wn = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ship_icon.png")
pygame.display.set_icon(icon)

# images
background = pygame.image.load("images/background.png")
ship = pygame.image.load("images/space-ship.png")
bullet = pygame.image.load("images/bullet.png")

# ship
ship_x = 370
ship_y = 480
ship_dx = 0

# bullet
bullet_x = ship_x + 16
bullet_y = ship_y
bullet_dy = 0

# invaders
invader_img = []
invader_x = []
invader_y = []
invader_dx = []
num_invaders = 7

for i in range(num_invaders):
    invader_img.append(pygame.image.load("images/enemy.png"))
    invader_x.append(random.randint(11, 730))
    invader_y.append(random.randint(11, 60))
    invader_dx.append(5)

# text
score = 0
score_font = pygame.font.Font("freesansbold.ttf", 25)
over_font = pygame.font.Font("freesansbold.ttf", 70)

# main loop
running = True
while running:
    pygame.display.update()

    # images
    wn.blit(background, (0, 0))
    wn.blit(bullet, (bullet_x, bullet_y))
    wn.blit(ship, (ship_x, ship_y))
    for i in range(num_invaders):
        wn.blit(invader_img[i], (invader_x[i], invader_y[i]))

    # screen events
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                ship_dx -= 12
            if i.key == pygame.K_RIGHT:
                ship_dx += 12
            if i.key == pygame.K_UP:
                fire_sound = pygame.mixer.Sound("sounds/laser.wav")
                fire_sound.play()
                bullet_dy -= 25
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                ship_dx = 0

    # ship movement
    ship_x += ship_dx
    if ship_x > 736:
        ship_x = 736
    if ship_x < 4:
        ship_x = 4

    # bullet movement
    bullet_y += bullet_dy
    if not bullet_dy < 0:
        bullet_x = ship_x + 16

    if bullet_y < 0:
        bullet_x = ship_x + 16
        bullet_y = ship_y
        bullet_dy = 0

    for i in range(num_invaders):
        invader_x[i] += invader_dx[i]
        if invader_x[i] > 740 or invader_x[i] < 10:
            invader_dx[i] *= -1
            invader_y[i] += 40

        if bullet_y < invader_y[i] + 20 and (invader_x[i] + 40 > bullet_x > invader_x[i] - 20):
            explode = pygame.mixer.Sound("sounds/explosion.wav")
            explode.play()
            bullet_x = ship_x + 16
            bullet_y = ship_y
            bullet_dy = 0
            score += 1
            invader_x[i] = random.randint(11, 730)
            invader_y[i] = random.randint(11, 60)

        if invader_y[i] > 440:
            ship_y = 1000
            bullet_y = 10000
            for j in range(num_invaders):
                invader_y[j] = 2000
            over_text = over_font.render("GAME OVER!", True, (255, 144, 0))
            wn.blit(over_text, (180, 250))
            break

    # score board
    score_board = score_font.render("SCORE: " + str(score), True, (255, 220, 140))
    wn.blit(score_board, (14, 14))
