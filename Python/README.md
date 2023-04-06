## Description

Project consists of 4 files
-CreateDataset.py creates a random dataset of 10,000 vectors. Each vector consists of 40 elements, where the first 39 are features, and the 40th element is the expected outcome.
-NeuralNetwork.py is where the layers of the neural network are defined.
-trainer.py is the main file of the project. It consists of a training loop and a testing loop.
-visualization.py is a simple script used to print out learning diagrams.

## Requirements

- Python3.7+
- [Biblioteka pytorch](https://pytorch.org/get-started/locally/). As a Compute Platform it is recommended to choose CPU as it is smaller.

## Usage

To run the project, download the repository and ensure that all files are in the same directory. First, run CreateDataset.py using the following command:
```
python CreateDataset.py
```
Once the "data.csv" file has been created, run trainer.py using the following command:
```
python trainer.py
```
Remember to ensure that you have the necessary dependencies installed before running the program.

## Output
As an output of the project, you should receive 2 .png files that show the learning curve of the neural network. Example files have been added to the "test" folder.

Note that this neural network is for demonstration purposes only. Since the data is created randomly in CreateDataset.py, the accuracy of the NeuralNetwork is expected to be around 50%.

## Author

Mateusz Boruch
mateuszboruch1992@gmail.com