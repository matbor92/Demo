from NeuralNetwork import Net
import torch
import torch.nn as nn
import torch.optim as optim
from visualization import plot_accuracy, plot_running_loss

import pandas as pd
import matplotlib.pyplot as plt

torch.manual_seed(1234)
model = Net()

# Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
num_epochs = 10

# Loading data from data.csv
data = pd.read_csv('data.csv')
inputs = torch.tensor(data.iloc[:, :-1].values, dtype=torch.float32)
targets = torch.tensor(data.iloc[:, -1].values, dtype=torch.long)

# Dividing data to test and train set
train_size = int(0.75 * len(inputs))
test_size = len(inputs) - train_size
train_inputs, test_inputs = torch.split(inputs, [train_size, test_size], dim=0)
train_targets, test_targets = torch.split(targets, [train_size, test_size], dim=0)

# Creation of DataLoaders for train and test sets
train_dataset = torch.utils.data.TensorDataset(train_inputs, train_targets)
test_dataset = torch.utils.data.TensorDataset(test_inputs, test_targets)
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=128, shuffle=True)
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=128, shuffle=False)

train_running_loss_list = []
test_accuracy_list = []
# Training loop
for epoch in range(num_epochs):
    running_loss = 0.0
    for i, data in enumerate(train_dataloader, 0):
        inputs, targets = data
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        if i % 10 == 9:
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 10))
            train_running_loss_list.append(running_loss / len(train_dataloader))
            running_loss = 0.0

    # Test loop
    correct = 0
    total = 0
    with torch.no_grad():
        for data in test_dataloader:
            inputs, targets = data
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()
            test_accuracy_list.append(100 * correct / total)
    print('[Epoch %d] test_accuracy: %.3f%%' % (epoch + 1, 100 * correct / total))

plot_accuracy(test_accuracy_list)
plot_running_loss(train_running_loss_list)
