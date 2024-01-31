import pygame

from random import randint

class SnakeGame():
    def __init__(self):
        # Initialises all PyGame modules
        pygame.init()

        # Initialise game over condition.
        self.game_over = False

        self.DIS_W, self.DIS_H = 600, 400

        self.SNAKE_SIZE = 10

        self.x1 = self.DIS_W/2
        self.y1 = self.DIS_H/2
        
        self.x1_change = 0
        self.y1_change = 0

        self.snake_list = []
        self.snake_list_length = 1

        # Creates a surface from a given tuple
        self.DIS=pygame.display.set_mode((self.DIS_W, self.DIS_H)) # y, x

        # Sets caption for window.
        pygame.display.set_caption('Snake')

        # Set variables and constants used later on
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.clock = pygame.time.Clock()

        self.foodx = round(randint(0, self.DIS_W - self.SNAKE_SIZE) / 10) * 10
        self.foody = round(randint(0, self.DIS_H - self.SNAKE_SIZE) / 10) * 10

    def boundary_check(self):
        if self.x1 >= self.DIS_W or self.x1 < 0 or self.y1 >= self.DIS_H or self.y1 < 0:
            self.game_over = True
        else:
            pass

    def food_graphics(self):
        # Food coord/size list
        food_list = [self.foodx,
                     self.foody, 
                     self.SNAKE_SIZE, 
                     self.SNAKE_SIZE]

        # Food (rectangle object)
        pygame.draw.rect(self.DIS, self.WHITE, food_list)

        #pygame.display.update()

    def snake(self):

        # Snake (rectangle object)
        snake_head = []
        snake_head.append(self.x1)
        snake_head.append(self.y1)
        self.snake_list.append(snake_head)
        
        if len(self.snake_list) > self.snake_list_length:
            del self.snake_list[0]
 
        for x in self.snake_list[:-1]:
            if x == snake_head:
                self.game_over = True

        for x in self.snake_list:
            pygame.draw.rect(self.DIS, self.BLUE, [x[0], x[1], self.SNAKE_SIZE, self.SNAKE_SIZE])

        #pygame.display.update()
    
    def game_main_loop(self):
        while not self.game_over:

            for event in pygame.event.get():
                # This if statement allows us to click the quit
                # button on the window and close the program.
                if event.type==pygame.QUIT:
                    self.game_over = True

                # Key stroke event management
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.x1_change = -self.SNAKE_SIZE
                        self.y1_change = 0
                    elif event.key == pygame.K_d:
                        self.x1_change = self.SNAKE_SIZE
                        self.y1_change = 0
                    elif event.key == pygame.K_w:
                        self.y1_change = -self.SNAKE_SIZE
                        self.x1_change = 0
                    elif event.key == pygame.K_s:
                        self.y1_change = self.SNAKE_SIZE
                        self.x1_change = 0
                    elif event.type == pygame.QUIT:
                        self.game_over = True

            # Boundary condition checking
            self.boundary_check()

            # Ammending Coords of Snake
            self.x1 += self.x1_change
            self.y1 += self.y1_change

            # Re-fill display black
            self.DIS.fill(self.BLACK)

            # Food Creation/Graphics
            self.food_graphics()

            # Snake graphics
            self.snake()

            # Has the snake eaten
            if self.x1 == self.foodx and self.y1 == self.foody:
                self.foodx = round(randint(0, self.DIS_W - self.SNAKE_SIZE) / 10) * 10
                self.foody = round(randint(0, self.DIS_H - self.SNAKE_SIZE) / 10) * 10
                self.snake_list_length = self.snake_list_length + 1

            pygame.display.update()

            # means that for every second at most X frames should pass.
            # X being clock.tick(X)
            self.clock.tick(10)
        
        # Score
        self.score = self.snake_list_length - 1
        #print(self.score)

if __name__ == "__main__":
    snake_run = SnakeGame()
    snake_run.game_main_loop()


