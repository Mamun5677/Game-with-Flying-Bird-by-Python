import pygame
import sys
from pygame.math import Vector2
import random
import time


class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)
        self.apple = pygame.image.load("images/apple.png")

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        wn.blit(pygame.transform.scale(self.apple, (20, 20)), fruit_rect)


class Snake:
    def __init__(self):
        self.body = [Vector2(4, 10), Vector2(3, 10), Vector2(2, 10)]
        self.direction = None
        self.movement = "null"

        self.body_bl = pygame.image.load("images/body_bl.png")
        self.body_br = pygame.image.load("images/body_br.png")
        self.body_horizontal = pygame.image.load("images/body_horizontal.png")
        self.body_vertical = pygame.image.load("images/body_vertical.png")
        self.body_tl = pygame.image.load("images/body_tl.png")
        self.body_tr = pygame.image.load("images/body_tr.png")
        self.head_down = pygame.image.load("images/head_down.png")
        self.head_up = pygame.image.load("images/head_up.png")
        self.head_left = pygame.image.load("images/head_left.png")
        self.head_right = pygame.image.load("images/head_right.png")
        self.tail_up = pygame.image.load("images/tail_up.png")
        self.tail_down = pygame.image.load("images/tail_down.png")
        self.tail_left = pygame.image.load("images/tail_left.png")
        self.tail_right = pygame.image.load("images/tail_right.png")

        self.head = None
        self.tail = None

    def draw_snake(self):
        self.image_update()

        for k, j in enumerate(self.body):
            snake_rect = pygame.Rect(int(j.x * cell_size), int(j.y * cell_size), cell_size, cell_size)
            if k == 0:
                wn.blit(pygame.transform.scale(self.head, (20, 20)), snake_rect)
            elif k == len(self.body) - 1:
                wn.blit(pygame.transform.scale(self.tail, (20, 20)), snake_rect)
            else:
                body_relation = self.body[k] - self.body[k + 1]
                body_relation1 = self.body[k] - self.body[k - 1]

                if (body_relation == Vector2(-1, 0) and body_relation1 == Vector2(0, -1)) or \
                        (body_relation == Vector2(0, -1) and body_relation1 == Vector2(-1, 0)):
                    wn.blit(pygame.transform.scale(self.body_br, (20, 20)), snake_rect)
                elif (body_relation == Vector2(1, 0) and body_relation1 == Vector2(0, -1)) or \
                        (body_relation == Vector2(0, -1) and body_relation1 == Vector2(1, 0)):
                    wn.blit(pygame.transform.scale(self.body_bl, (20, 20)), snake_rect)

                elif (body_relation == Vector2(-1, 0) and body_relation1 == Vector2(0, 1)) or \
                        (body_relation == Vector2(0, 1) and body_relation1 == Vector2(-1, 0)):
                    wn.blit(pygame.transform.scale(self.body_tr, (20, 20)), snake_rect)
                elif (body_relation == Vector2(1, 0) and body_relation1 == Vector2(0, 1)) or \
                        (body_relation == Vector2(0, 1) and body_relation1 == Vector2(1, 0)):
                    wn.blit(pygame.transform.scale(self.body_tl, (20, 20)), snake_rect)

                elif body_relation == Vector2(1, 0) or body_relation == Vector2(-1, 0):
                    wn.blit(pygame.transform.scale(self.body_horizontal, (20, 20)), snake_rect)
                elif body_relation == Vector2(0, 1) or body_relation == Vector2(0, -1):
                    wn.blit(pygame.transform.scale(self.body_vertical, (20, 20)), snake_rect)

    def move_snake(self):
        if self.movement != "null":
            if len(self.body) == 1:
                self.body[0] += self.direction
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]

    def image_update(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        if head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.fruit_collision()
        self.border_collision()
        self.body_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.score_board()

    def fruit_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.pos.x = random.randint(0, cell_num - 1)
            self.fruit.pos.y = random.randint(0, cell_num - 1)
            self.snake.body.append(self.snake.body[-1])

    def border_collision(self):
        if self.snake.body[0].x > cell_num - 1:
            self.snake.body[0].x = -1
        if self.snake.body[0].x < -1:
            self.snake.body[0].x = cell_num
        if self.snake.body[0].y > cell_num - 1:
            self.snake.body[0].y = -1
        if self.snake.body[0].y < -1:
            self.snake.body[0].y = cell_num

    def body_collision(self):
        if len(self.snake.body) > 2:
            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    time.sleep(0.5)
                    self.snake.movement = "null"
                    self.snake.body = [Vector2(4, 10), Vector2(3, 10), Vector2(2, 10)]

    def score_board(self):
        text = font.render(str(len(self.snake.body) - 3), True, (56, 74, 12))
        score_pos = int(cell_size * cell_num - 35)
        score_rect = text.get_rect(topright=(score_pos, score_pos))
        apple_rect = self.fruit.apple.get_rect(midright=(score_rect.left + 16, score_rect.bottom))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width - 10,
                              apple_rect.height - 18)
        pygame.draw.rect(wn, (90, 150, 19), bg_rect, 2)
        wn.blit(text, score_rect)
        wn.blit(pygame.transform.scale(self.fruit.apple, (20, 20)), apple_rect)


def grass():
    grass_color = (150, 235, 60)
    gx = 0
    gy = 0
    for z in range(cell_num):
        for y in range(cell_num // 2):
            grass_rect = pygame.Rect(gx, gy, cell_size, cell_size)
            pygame.draw.rect(wn, grass_color, grass_rect)
            gx += 40
        if z % 2 == 0:
            gx = 20
        else:
            gx = 0
        gy += 20


pygame.init()
cell_size = 20
cell_num = 22
wn = pygame.display.set_mode((cell_size * cell_num, cell_size * cell_num))
icon = pygame.image.load("images/snake32.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 22)

main_game = Main()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == screen_update:
            main_game.update()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                if main_game.snake.movement != "down":
                    main_game.snake.direction = Vector2(0, -1)
                    main_game.snake.movement = "up"
            if i.key == pygame.K_DOWN:
                if main_game.snake.movement != "up":
                    main_game.snake.direction = Vector2(0, 1)
                    main_game.snake.movement = "down"
            if i.key == pygame.K_LEFT:
                if main_game.snake.movement != "right":
                    main_game.snake.direction = Vector2(-1, 0)
                    main_game.snake.movement = "left"
            if i.key == pygame.K_RIGHT:
                if main_game.snake.movement != "left":
                    main_game.snake.direction = Vector2(1, 0)
                    main_game.snake.movement = "right"

    wn.fill((175, 215, 70))
    grass()
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
