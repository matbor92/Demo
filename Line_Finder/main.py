from CreateDataset import generate_img
import torch
import torch.nn as nn
import torch.optim as optim
import os
from datetime import datetime
from neural_network import LineCoordinatesNet
from visualization import plot_statistics


def init():
    # inicjalizacja modelu, funkcji straty i optimizera
    model = LineCoordinatesNet()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.SmoothL1Loss(reduction='mean')

    # funkcja generująca i zapisujaca przykładowe pliki wejściowe.
    # Jakby ktoś chciał podpatrzeć jak wygląda wejście, to należy ją odkomentować :)
    # generate_img(10, save_file=True)

    return model, optimizer, criterion


# funkcja zapisująca model
def save_model(model):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = 'output'
    os.makedirs(folder_name, exist_ok=True)
    file_name = f'{folder_name}/model_{current_datetime}.pt'
    torch.save(model.state_dict(), file_name)


def test_accuracy(model):
    num_test_images = 100
    correct_predictions = 0

    inputs, labels = generate_img(num_test_images)  # Generowanie testowego zestawu danych
    inputs_tensor = torch.stack(inputs)
    outputs = model(inputs_tensor).float()
    predictions = outputs.round().long()  # Zaokrąglenie wyjść do najbliższych wartości całkowitych

    for predictions, label in zip(predictions, labels):
        errors = torch.abs(predictions - label)
        if torch.sum(errors) <= 20:
            correct_predictions += 1

    accuracy = correct_predictions * 100 / num_test_images
    return accuracy


def training_loop():
    net, optimizer, criterion = init()
    num_epochs = 90
    batch_size = 128
    train_running_loss_list = []
    train_accuracy_list = []
    for epoch in range(num_epochs):
        inputs, y_label = generate_img(batch_size)

        # Wyczyszczenie gradientów parametrów
        optimizer.zero_grad()

        # Przejście przez sieć
        inputs_tensor = torch.stack(inputs)
        outputs = net(inputs_tensor).float()
        # print("---------------------OUTPUTS------------------------")
        # print(outputs)

        # Obliczenie straty
        loss = criterion(outputs, y_label)

        # Propagacja wsteczna i aktualizacja wag
        loss.backward()
        optimizer.step()

        # Wyświetlanie informacji o bieżącej epoce, wartości błędu, oraz dokładności sieci
        accuracy = test_accuracy(net)
        print(f"Epoch: {epoch + 1}, Loss: {loss.item()}, Accuracy: {accuracy}%")
        train_running_loss_list.append(loss.item())
        train_accuracy_list.append(accuracy)

    plot_statistics(train_running_loss_list, train_accuracy_list)
    save_model(net)

if __name__ == '__main__':
    training_loop()
