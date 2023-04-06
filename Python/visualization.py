import matplotlib.pyplot as plt

def plot_accuracy(test_accuracy_list):
    plt.plot(range(len(test_accuracy_list)), test_accuracy_list)
    plt.ylabel('%')
    plt.title('Test accuracy')
    plt.savefig('Test accuracy')

def plot_running_loss( train_running_loss_list):
    plt.plot(range(len( train_running_loss_list)),  train_running_loss_list)
    plt.title('Running loss')
    plt.savefig('Running loss')