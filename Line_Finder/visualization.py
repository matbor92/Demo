import matplotlib.pyplot as plt
import os
from datetime import datetime

def plot_statistics(train_running_loss_list, train_accuracy_list):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Pobranie aktualnej daty i godziny
    folder_name = 'output'
    os.makedirs(folder_name, exist_ok=True)  # Utworzenie folderu "output", jeśli nie istnieje
    file_name = f'{folder_name}/Loss_Accuracy_{current_datetime}.png'  # Zbudowanie nazwy pliku z datą i godziną

    plt.figure(figsize=(10, 8))  # Utworzenie nowej figury o większych wymiarach
    plt.subplot(2, 1, 1)  # Pierwszy wykres (loss)
    plt.plot(range(len(train_running_loss_list)), train_running_loss_list)
    plt.title('Running loss')
    plt.ylabel('Loss Value')
    plt.xlabel('Epochs')

    plt.subplot(2, 1, 2)  # Drugi wykres (accuracy)
    plt.plot(range(len(train_accuracy_list)), train_accuracy_list)
    plt.title('Accuracy')
    plt.ylabel('Accuracy (%)')
    plt.xlabel('Epochs')

    plt.tight_layout()  # Dostosowanie układu wykresów
    plt.savefig(file_name)