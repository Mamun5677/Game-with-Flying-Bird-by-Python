import pygame
import sys
import random

pygame.init()
wn = pygame.display.set_mode((360, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

bg_img = pygame.image.load("images/background-day.png").convert_alpha()
background = pygame.transform.scale(bg_img, (360, 500))

floor_img = pygame.image.load("images/base.png").convert_alpha()
floor = pygame.transform.scale(floor_img, (360, 112))
floor_x = 0

blue_bird_upflap = pygame.image.load(
    "images/bluebird-upflap.png").convert_alpha()
blue_bird_midflap = pygame.image.load(
    "images/bluebird-midflap.png").convert_alpha()
blue_bird_downflap = pygame.image.load(
    "images/bluebird-downflap.png").convert_alpha()
blue_bird_list = [blue_bird_upflap, blue_bird_midflap, blue_bird_downflap]
blue_bird = blue_bird_upflap
blue_bird_rect = blue_bird.get_rect(center=(50, 240))
gravity = 0.25
bird_dy = 0

red_bird = pygame.image.load("images/redbird-downflap.png").convert_alpha()
pygame.display.set_icon(red_bird)

pipe_img = pygame.image.load("images/pipe-green.png").convert_alpha()
pipe_surface = pygame.transform.scale(pipe_img, (40, 250))

pipes = [pipe_surface.get_rect(bottomright=(220, 490)), pipe_surface.get_rect(bottomright=(
    420, 600)), pipe_surface.get_rect(bottomright=(220, 70)), pipe_surface.get_rect(bottomright=(420, 180))]
pipe_height = [490, 600, 460]

intro_pic = pygame.image.load("images/message.png").convert_alpha()
intro_img = pygame.transform.scale(intro_pic, (360, 500))

game_over_img = pygame.image.load("images/gameover.png").convert_alpha()

font = pygame.font.Font(None, 20)
font1 = pygame.font.Font(None, 28)

score = 0
highscore = 0

game_state = False
game_over = False

timer1 = pygame.USEREVENT
pygame.time.set_timer(timer1, 3000)

timer2 = pygame.USEREVENT
pygame.time.set_timer(timer2, 300)
count = 1


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_dy * 2, 1)
    return new_bird


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird_dy = 0
                bird_dy -= 8
            if event.key == pygame.K_SPACE and game_state == False:
                game_state = True
                pipes = [pipe_surface.get_rect(bottomright=(220, 490)), pipe_surface.get_rect(bottomright=(
                    220, 70)), pipe_surface.get_rect(bottomright=(420, 600)), pipe_surface.get_rect(bottomright=(420, 180))]
                blue_bird_rect.centery = 240
                bird_dy = 0
                score = 0

        if event.type == timer1:
            random_pos = random.choice(pipe_height)
            bottom_pipe = pipe_surface.get_rect(
                bottomright=(pipes[-1].centerx + 200, random_pos))
            top_pipe = pipe_surface.get_rect(bottomright=(
                pipes[-1].centerx + 200, random_pos - 420))
            pipes.append(bottom_pipe)
            pipes.append(top_pipe)

        if event.type == timer2:
            blue_bird = blue_bird_list[count]
            count += 1
            if count == 3:
                count = 0

    wn.blit(background, (0, 0))
    if game_state:
        rotated_blue_bird = rotate_bird(blue_bird)
        wn.blit(rotated_blue_bird, blue_bird_rect)
        bird_dy += gravity
        blue_bird_rect.centery += bird_dy

        for i in pipes:
            if i.bottom > 400:
                wn.blit(pipe_surface, i)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                wn.blit(flip_pipe, i)
            i.centerx -= 1

        if pipes[score].right < blue_bird_rect.left:
            score += 1
            if score >= highscore:
                highscore = score

        text = font.render("SCORE: " + str(int(score/2)) + "   HIGH SCORE: " +
                           str(int(highscore/2)), True, pygame.Color("brown"))
        wn.blit(text, (10, 10))
    else:
        if game_over:
            wn.blit(game_over_img, (80, 230))
            intro_text = font1.render("press SPACE to play", True, (0, 30, 69))
            wn.blit(intro_text, (85, 360))
        else:
            wn.blit(intro_pic, (88, 80))
            wn.blit(red_bird, (163.4, 249.4))
            intro_text = font1.render("press SPACE to play", True, (0, 30, 69))
            wn.blit(intro_text, (85, 360))

    wn.blit(floor, (floor_x, 420))
    wn.blit(floor, (floor_x + 360, 420))
    floor_x -= 1
    if floor_x == -360:
        floor_x = 0

    for i in pipes:
        if blue_bird_rect.colliderect(i):
            game_over = True
            game_state = False
        if blue_bird_rect.y < -40 or blue_bird_rect.y > 440:
            game_over = True
            game_state = False

    pygame.display.update()
    clock.tick(60)
