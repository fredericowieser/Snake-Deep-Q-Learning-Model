import os

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class LinearQNet(nn.Module):
    """
    Our Neural Network based on 2 layers.
    """
    def __init__(self, input_size, hidden_size, output_size) -> None:
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
    
    def save(self, file_name='model.pth'):
        model_path = './model'
        if not os.path.exists(model_path):
            os.makedirs(model_path)

        file_name = os.path.join(model_path, file_name)
        torch.save(self.state_dict(), file_name)


class QTrainer:
    """
    Training Class for our Neural Network.
    """
    def __init__(self, model, lr, gamma) -> None:
        self.lr = lr
        self.gamma = gamma
        self.model = model

        self.optim = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        # Handle any size (tuple or single) state, etc.
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        # Data.shape = (n, x)

        if len(state.shape) == 1:
            # Data.shape = (1, x) 
            # Remove values from tensor wrappers
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, ) # One value tuple

        # 1: predicted Q values with current state
        Q_pred = self.model(state)

        target = Q_pred.clone()
        # Iterate over our tensors 
        for idx in range(len(done)):
            Q_new = reward[idx]

            # If event (state, etc.) was not done 
            if not done[idx]:
                # Bellman Equation
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))

            target[idx][torch.argmax(action[idx]).item()] = Q_new
    
        # 2: Q_new = r + y * max(next_predicted Q value) -> only do this if not done
        # pred.clone()
        # preds[argmax(action)] = Q_new
        
        # Empty Gradients?? (PyTorch Weirdnedd)
        self.optim.zero_grad()

        # Calc Loss
        loss = self.criterion(target, Q_pred)

        # Apply Backprop & Update out Gradients
        loss.backward()

        self.optim.step()