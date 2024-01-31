# Python Snake AI

Reference:
[Python + PyTorch + Pygame Reinforcement Learning - Train an AI to Play Snake](https://www.youtube.com/watch?v=L8ypSXwyBds)

### Reinforcement Learning

RL is an area of ML concerned with how software agents ought to take action in an enviorment in order to maximize the notion of cumulative reward.

In this case we will use Deep Q Learning, an approach that extends reinforcement learning by using a deep neural network to predict the actions.

![Screenshot 2022-11-15 at 14-41-14 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_14-41-14_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

In this case we will be using the following rules…

![Screenshot 2022-11-15 at 14-56-12 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_14-56-12_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

![Screenshot 2022-11-15 at 15-06-33 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_15-06-33_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

![Screenshot 2022-11-15 at 15-06-56 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_15-06-56_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

Using these as our possible states, actions and rewards we can now come up with a model…

![Screenshot 2022-11-15 at 15-14-40 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_15-14-40_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

![Screenshot 2022-11-15 at 15-16-04 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_15-16-04_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

![Screenshot 2022-11-15 at 15-19-24 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_15-19-24_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

![Screenshot 2022-11-15 at 15-19-53 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_15-19-53_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

![Screenshot 2022-11-15 at 15-20-20 Python PyTorch Pygame Reinforcement Learning – Train an AI to Play Snake.png](Screenshot_2022-11-15_at_15-20-20_Python_PyTorch_Pygame_Reinforcement_Learning__Train_an_AI_to_Play_Snake.png)

### Setup Environment and Implement Snake

```bash
$ conda create -n pygame_env python=3.7
```

Once our environment is created we can activate it via…

```bash
$ conda activate pygame_env
```

Once we are working in our environment we must retrieve the packages we will be using in this game.

```bash
pygame pytorch matplotlib ipython
```

Pytorch can’t be installed this simply and requires the user to go to the website and download the required pytorch packages for their use case scenario…

In this case

```bash
$ pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
```

### Snake Game Development

[Snake Game in Python | Snake Game Program using Pygame | Edureka](https://www.edureka.co/blog/snake-game-with-pygame/)

In this we will be creating our version of snake trying to follow from online resources. This is because in the tutorial this project is based on the instructor uses a premade snake game that they have already worked on. I would argue this removes some of the fun out of the project and therefore will be reintroducing this by creating out own snake game and adapting the tutorial to fit our snake game.

We will be using the link put at the start of this chapter as our guide in creating this snake game.

First we look at some of the functions we will be utilizing in this game…

![Screenshot 2022-11-15 at 16-07-39 Snake Game in Python Snake Game Program using Pygame Edureka.png](Screenshot_2022-11-15_at_16-07-39_Snake_Game_in_Python_Snake_Game_Program_using_Pygame_Edureka.png)

### New PyGame Window

To start off with we are going to create a basic PyGame window to test that our environment is suitable for working and developing our game and that is able to run.

This basic pygame window is produced via…

```python
import pygame

# Initialises all pygame modules
pygame.init()

# Creates a surface from a given tuple
dis=pygame.display.set_mode((400,300))

# Updates screen
pygame.display.update()

pygame.quit()
quit()
```

In our system this code would not execute when we were inside a virtual environment, even with all packages loaded. Error being this…

```
pygame 2.1.2 (SDL 2.0.16, Python 3.9.13)
Hello from the pygame community. https://www.pygame.org/contribute.html
libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: iris
libGL error: MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: swrast
X Error of failed request:  BadValue (integer parameter out of range for operation)
  Major opcode of failed request:  149 (GLX)
  Minor opcode of failed request:  3 (X_GLXCreateContext)
  Value in failed request:  0x0
  Serial number of failed request:  105
  Current serial number in output stream:  106
```

To fix this we escaped the virtual environment as other sources stated this solved the issue…

[Problem with PyGame - libGL error: failed to load driver: swrast](https://askubuntu.com/questions/1392138/problem-with-pygame-libgl-error-failed-to-load-driver-swrast)

With this in mind we will now no longer be utilising our virtual environment when developing the game but recommend other users to do so.

You can escape your virtual environment by using…

```bash
$ conda deactivate
```

### PyGame Further Setup

To move the snake, you will need to use the key events present in the KEYDOWN class of Pygame. The events that are used over here are, K_UP, K_DOWN, K_LEFT, and K_RIGHT to make the snake move up, down, left and right respectively. Also, the display screen is changed from the default black to white using the *fill()* method.

I have created new variables *x1_change* and *y1_change* in order to hold the updating values of the x and y coordinates.

We will also now be updating our initial definition of the size of the PyGame window, to be a sixth of the size of our monitor in terms of pixels and be placed in the centre. To do this we will use “`w, h = pygame.display.get_surface().get_size()`"

From…

[How to get the resolution of a monitor in Pygame?](https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame)

[pygame clock.tick() vs framerate in game main loop](https://stackoverflow.com/questions/34383559/pygame-clock-tick-vs-framerate-in-game-main-loop)

### CODE

```python
import pygame

# Initialises all PyGame modules
pygame.init()

# Get size of monitor
infoObject = pygame.display.Info()
SCREEN_W, SCREEN_H = infoObject.current_w, infoObject.current_h

# Creates a surface from a given tuple
DIS=pygame.display.set_mode((SCREEN_W/4, SCREEN_H/4)) # y, x

# Sets caption for window.
pygame.display.set_caption('Snake')

# Set variables and constants used later on
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialise game over condition.
game_over=False

x1 = SCREEN_W/8
y1 = SCREEN_H/8
 
x1_change = 0
y1_change = 0
 
clock = pygame.time.Clock()

# MAIN, GAME LOOP
while not game_over:
    for event in pygame.event.get():

        # This if statement allows us to click the quit
        # button on the window and close the program.
        if event.type==pygame.QUIT:
            game_over = True

        # Key stroke event management
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
        
    x1 += x1_change
    y1 += y1_change

        #prints out all the actions that take place on the screen
        #print(event)
    
    # Re-fill display black
    DIS.fill(BLACK)
    
    # Snake (rectangle object)
    pygame.draw.rect(DIS, BLUE, [x1, y1, 10, 10])

    # Updates screen
    pygame.display.update()

    # means that for every second at most X frames should pass.
    # X being clock.tick(X)
    clock.tick(10)
    

# Quit PyGame and Python
pygame.quit()
quit()
```

### Adding Boundary Conditions, Food, and Increasing Snake Length

### CODE

```python
from random import randint
import pygame

# Initialises all PyGame modules
pygame.init()

# Get size of monitor
infoObject = pygame.display.Info()
SCREEN_W, SCREEN_H = infoObject.current_w, infoObject.current_h

DIS_W, DIS_H = SCREEN_W/4, SCREEN_H/4

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

    foodx = randint(0, DIS_W - SNAKE_SIZE)
    foody = randint(0, DIS_H - SNAKE_SIZE)

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
            foodx = randint(0, DIS_W - SNAKE_SIZE)
            foody = randint(0, DIS_H - SNAKE_SIZE)
            snake_list_length = snake_list_length + 1

        # means that for every second at most X frames should pass.
        # X being clock.tick(X)
        clock.tick(10)

game_loop()
```

The problems we have encountered at this point in the project are that the code executes correctly but does not seem to register when food is “eaten”. Meaning that our snake never grows. With this we need to find a way to solve this bug. We didn’t take the last step of tracking the score but this is easy as the score is just the length of the snake - 1. That means that proceeding in this project we are going to do 3 things…

- Fix “Eating” Bug, perhaps with looser definitions of box/check if tutorials code works
- Convert the current procedural program to an OOP format.
- Create a score tracking system

### CODE (after OOP and bug correction)

```python
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
```

### Adapting Snake Game for Deep Q Learning

Using our current Snake game we now want to implement the following code and features into the game in order to be ready for the training.

- Reset Game function, so that after each game the agent can reset the game.
- Implement the reward system for the agent
- play function  that computes direction
- keep track of current game itteration
- is_collision function