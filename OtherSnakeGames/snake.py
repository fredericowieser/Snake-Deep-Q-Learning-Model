from random import randint
import pygame
#

# Initialises all PyGame modules
pygame.init()

# Get size of monitor
infoObject = pygame.display.Info()
SCREEN_W, SCREEN_H = infoObject.current_w, infoObject.current_h

#DIS_W, DIS_H = round(SCREEN_W/10)*10, round(SCREEN_H/10)*10
DIS_W, DIS_H = 600, 400

# Creates a surface from a given tuple
DIS=pygame.display.set_mode((DIS_W, DIS_H)) # y, x

# Sets caption for window.
pygame.display.set_caption('Snake')

# Set variables and constants used later on
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SNAKE_SIZE = 10
font_style = pygame.font.SysFont(None, 15)
score_font = pygame.font.SysFont("comicsansms", 35)

clock = pygame.time.Clock()

def our_snake(SNAKE_SIZE, snake_list):
    for x in snake_list:
        pygame.draw.rect(DIS, BLUE, [x[0], x[1], SNAKE_SIZE, SNAKE_SIZE])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    DIS.blit(mesg, [DIS_W/3, DIS_H/3])

def game_loop():
    # Initialise game over condition.
    game_over = False
    game_close = False

    x1 = DIS_W/2
    y1 = DIS_H/2
    
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_list_length = 1

    foodx = round(randint(0, DIS_W - SNAKE_SIZE) / 10) * 10
    foody = round(randint(0, DIS_H - SNAKE_SIZE) / 10) * 10

    # MAIN, GAME LOOP
    while not game_over:

        while game_close == True:
            DIS.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False


        for event in pygame.event.get():

            # This if statement allows us to click the quit
            # button on the window and close the program.
            if event.type==pygame.QUIT:
                game_over = True

            # Key stroke event management
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -SNAKE_SIZE
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = SNAKE_SIZE
                    x1_change = 0
        
        # Boundary condition checking
        if x1 >= DIS_W or x1 < 0 or y1 >= DIS_H or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

            #prints out all the actions that take place on the screen
            #print(event)
        
        # Re-fill display black
        DIS.fill(BLACK)

        # Food (rectangle object)
        pygame.draw.rect(DIS, WHITE, [foodx, foody, SNAKE_SIZE, SNAKE_SIZE])

        # Snake (rectangle object)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_list_length:
            del snake_list[0]
 
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
 
        our_snake(SNAKE_SIZE, snake_list)

        # Updates screen
        pygame.display.update()

        # Has the snake eaten
        if x1 == foodx and y1 == foody:
            foodx = round(randint(0, DIS_W - SNAKE_SIZE) / 10) * 10
            foody = round(randint(0, DIS_H - SNAKE_SIZE) / 10) * 10
            snake_list_length = snake_list_length + 1

        # means that for every second at most X frames should pass.
        # X being clock.tick(X)
        clock.tick(10)

game_loop()