import pygame
import time
import random

pygame.init()

display_width = 400
display_height = 400
display = pygame.display.set_mode((display_width,display_height))
pygame.display.update()

pygame.display.set_caption('Snake')

blue = (115, 189, 168)
red = (204, 107, 73)
yellow = (255, 255, 102)
green = (0, 255, 0)
white = (236, 230, 194)
black = (111, 86, 67)

snake_block = 40
snake_speed = 5

font_style = pygame.font.SysFont("bahnschrift", 30)

clock = pygame.time.Clock()

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [50, 10])

def player_snake(snake_block, snake_list):
    for unit in snake_list:
        pygame.draw.rect(display, blue, [unit[0], unit[1], snake_block, snake_block])

def player_score(score):
    num = font_style.render("Your Score: " + str(score), True, black)
    display.blit(num, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width/2
    y1 = display_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = snake_block * round(random.randrange(0, display_width - snake_block) / snake_block) # / 20.0
    food_y = snake_block * round(random.randrange(0, display_height - snake_block) / snake_block)

    while not game_over:
        while game_close == True:
            display.fill(white)
            message("You lost! Q: quit, C: play again", red)
            #player_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(white)

        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for unit in snake_list[:-1]:
            if unit == snake_head:
                game_close = True
        
        player_snake(snake_block, snake_list)
        player_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = snake_block * round(random.randrange(0, display_width - snake_block) / snake_block)
            food_y = snake_block * round(random.randrange(0, display_height - snake_block) / snake_block)
            snake_length += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
