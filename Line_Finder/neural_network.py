import torch
import torch.nn as nn


class LineCoordinatesNet(nn.Module):
    def __init__(self):
        super(LineCoordinatesNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.classifier = nn.Sequential(
            nn.Linear(64 * 16 * 16, 256),
            nn.ReLU(),
            nn.Linear(256, 4),  # Wyjście sieci - współrzędne początku i końca linii
            nn.ReLU()  # Funkcja aktywacji ReLU
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        x = self.scale_output(x)  # Wywołanie metody do skalowania wyjścia
        return x

    def scale_output(self, output):
        min_value = torch.min(output)
        max_value = torch.max(output)
        range_value = max_value - min_value
        output_normalized = (output - min_value) / range_value
        output_scaled = output_normalized * 64
        return output_scaled