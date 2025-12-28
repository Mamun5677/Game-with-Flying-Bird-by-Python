import pygame

pygame.init()
wn = pygame.display.set_mode((660, 500))
pygame.display.set_caption("Pong")
font = pygame.font.Font("freesansbold.ttf", 20)

num_lines = 67
lines = []
line_x = 30
line_x1 = 30
line_y = 10
line_y1 = 10
line_y2 = 30
num = 0

for i in range(num_lines):
    if num < 12:
        rect = pygame.Rect(10, line_y, 5, 20)
        lines.append(rect)
        line_y += 40
    elif 11 < num < 24:
        rect = pygame.Rect(646, line_y1, 5, 20)
        lines.append(rect)
        line_y1 += 40
    elif 23 < num < 40:
        rect = pygame.Rect(line_x, 10, 20, 5)
        lines.append(rect)
        line_x += 40
    elif 39 < num < 56:
        rect = pygame.Rect(line_x1, 475, 20, 5)
        lines.append(rect)
        line_x1 += 40
    else:
        rect = pygame.Rect(330, line_y2, 5, 20)
        lines.append(rect)
        line_y2 += 40
    num += 1

paddle_a_y = 200
paddle_b_y = 200
paddle_a_dx = 0
paddle_b_dx = 0

ball = pygame.Surface((10, 10))
ball_x = 200
ball_y = 140
ball_x_dx = 0.38
ball_y_dx = 0.38

score_a = 0
score_b = 0

running = True
while running:
    pygame.display.update()
    wn.fill(pygame.Color("black"))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                paddle_b_dx = 0.4
            if i.key == pygame.K_DOWN:
                paddle_b_dx = -0.4
            if i.key == pygame.K_w:
                paddle_a_dx = 0.4
            if i.key == pygame.K_s:
                paddle_a_dx = -0.4
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_UP:
                paddle_b_dx = 0
            if i.key == pygame.K_DOWN:
                paddle_b_dx = 0
            if i.key == pygame.K_w:
                paddle_a_dx = 0
            if i.key == pygame.K_s:
                paddle_a_dx = 0

    for i in range(num_lines):
        pygame.draw.rect(wn, (255, 255, 255), lines[i])

    paddle_a_y -= paddle_a_dx
    paddle_b_y -= paddle_b_dx

    paddle_a = pygame.Rect(50, paddle_a_y, 10, 60)
    paddle_b = pygame.Rect(600, paddle_b_y, 10, 60)
    pygame.draw.rect(wn, (255, 255, 255), paddle_a)
    pygame.draw.rect(wn, (255, 255, 255), paddle_b)

    if paddle_a_y < 20 or paddle_a_y > 410:
        paddle_a_dx = 0
    if paddle_b_y < 20 or paddle_b_y > 410:
        paddle_b_dx = 0

    ball_x += ball_x_dx
    ball_y += ball_y_dx
    wn.blit(ball, (ball_x, ball_y))
    ball.fill(pygame.Color("white"))

    if ball_y > 470 or ball_y < 10:
        ball_y_dx *= -1
    if ball_x > 640:
        ball_x_dx *= -1
        ball_x = 300
        ball_y = 250
        score_a += 10
    if ball_x < 10:
        ball_x_dx *= -1
        ball_x = 300
        ball_y = 250
        score_b += 10
    if (45 < ball_x < 55) and (paddle_a_y - 10 < ball_y < paddle_a_y + 65):
        ball_x_dx *= -1
    if (595 < ball_x < 605) and (paddle_b_y - 10 < ball_y < paddle_b_y + 65):
        ball_x_dx *= -1

    score_board = font.render("SCORE: " + str(score_a) + "/100", True, (255, 255, 255))
    score_board1 = font.render("SCORE: " + str(score_b) + "/100", True, (255, 255, 255))
    wn.blit(score_board, (100, 60))
    wn.blit(score_board1, (430, 60))

    win_font = pygame.font.Font("freesansbold.ttf", 30)
    if score_a == 100:
        ball_x_dx = 0
        ball_y_dx = 0
        win = win_font.render("YOU WIN:)", True, (255, 255, 255))
        wn.blit(win, (100, 220))
    elif score_b == 100:
        ball_x_dx = 0
        ball_y_dx = 0
        win = win_font.render("YOU WIN:)", True, (255, 255, 255))
        wn.blit(win, (350, 220))
