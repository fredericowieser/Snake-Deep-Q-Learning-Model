import torch
import random
import numpy as np
from collections import deque
from game import SnakeGame, Direction, Point

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

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self):
        pass

    def get_action(self, state):
        pass

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
        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        
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


if __name__ == '__main__':
    train()

