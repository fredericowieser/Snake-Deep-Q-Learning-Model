import torch
import random
import numpy as np
from collections import deque
from game import SnakeGame, Direction, Point, BLOCK_SIZE

# These constants should be tested with for fine tuning
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self):
        self.n_games = 0 
        self.epsilon = 0 # Control of Randomness
        self.gamme = 0 # Discount Rate
        self.memory = deque(maxlen=MAX_MEMORY)
        
        # TODO: Model, Trainer
        self.model = None
        self.trainer = None

    def get_state(self, game):
        head = game.snake[0]
        
        # Points Around the Head
        point_l = Point(head.x - BLOCK_SIZE, head.y)
        point_r = Point(head.x + BLOCK_SIZE, head.y)
        point_u = Point(head.x, head.y - BLOCK_SIZE)
        point_d = Point(head.x, head.y + BLOCK_SIZE)
        
        # Current Game Direction, only one of these 4 can be true
        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            # Following 3 States are for danger
            # depending on movement of Snake head
            
            # Danger if we go straight ahead
            (dir_r and game.is_collision(point_r)) or 
            (dir_l and game.is_collision(point_l)) or 
            (dir_u and game.is_collision(point_u)) or 
            (dir_d and game.is_collision(point_d)),

            # Danger if we went right
            (dir_u and game.is_collision(point_r)) or 
            (dir_d and game.is_collision(point_l)) or 
            (dir_l and game.is_collision(point_u)) or 
            (dir_r and game.is_collision(point_d)),

            # Danger if we went left
            (dir_d and game.is_collision(point_r)) or 
            (dir_u and game.is_collision(point_l)) or 
            (dir_r and game.is_collision(point_u)) or 
            (dir_l and game.is_collision(point_d)),
            
            # Move direction (The direction we are moving)
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            
            # Food location (Where is the food relative to the Snake Head)
            game.food.x < game.head.x,  # food left
            game.food.x > game.head.x,  # food right
            game.food.y < game.head.y,  # food up
            game.food.y > game.head.y  # food down
        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        # Save to the Agent memory
        self.memory.append((state, action, reward, next_state, done)) # popleft if MAX_MEMORY is reached

    def train_short_memory(self, state, action, reward, next_state, done):
        # Takes one 
        self.trainer.train_step(state, action, reward, next_state, done)

    def train_long_memory(self):
        # If Agent memory size exceeds the BATCH_SIZE limit randomly sample to correct size
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # Returns list of tuples
        else:
            mini_sample = self.memory

        # Create 5 tuples from the batch and pass this for a batch training step
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
        
        # This should do the same as the code below...

        #for state, action, reward, nexrt_state, done in mini_sample:
        #    self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        # We want to have a probability of making random actions for exploration purposes
        # random moves: tradeoff exploration / exploitation

        # The more games we have the smaller epsilon gets until it become negative
        # and we no longer have any random moves.
        self.epsilon = 80 - self.n_games # Can change this for testing
        final_move = [0,0,0]
        # Random Move:
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1

        # Model Based Move:
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move

def train():
    plot_scores = []
    plot_mean_scores =[]
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGame()
    while True:
        # Get old state
        state_old = agent.get_state(game)

        # Get next action
        move = agent.get_action(state_old)

        # Perfrom move and get new state
        reward, done, score = game.play_step(move)
        state_new = agent.get_state(game)

        # Train short memory
        agent.train_short_memory(state_old, move, reward, state_new, done)
        
        # Remember
        agent.remember(state_old, move, reward, state_new, done)

        if done:
            # Train long memory and Plot the results
            # - Reset the game
            # - Increase Agent game counter
            # - Train the Agents Long term memory

            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            # If we got a new high score
            if score > record:
                record = score
                # agent.model.save()

            # Display Agent results
            print(
                f"Game: {agent.n_games}, Score: {score}, Record: {record}"
            )

            # Plotting Stuff...


if __name__ == '__main__':
    train()

