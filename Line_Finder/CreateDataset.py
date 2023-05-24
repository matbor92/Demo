import random
import torch
import torchvision.utils as vutils

def generate_img(batch_size, save_file = False):
    #inicjalizacja zmiennych wyjściowych funkcji
    grids = []
    line_tensors = []

    for i in range(batch_size):
        # Ustalanie rozmiaru obrazu
        image_size = 64

        # Tworzenie tensora wypełnionego wartościami 1 o rozmiarze (1, 3, image_size, image_size)
        # (1 - liczba obrazów, 3 - liczba kanałów koloru RGB)
        tensor = torch.ones(1, 3, image_size, image_size)

        #losowanie orientacji linii
        alignment = random.randint(0, 1)

        # Generowanie linii poziomej
        if alignment == 0:
            line_start_x = torch.randint(0, image_size - 1, (1,)).item()
            line_start_y = torch.randint(0, image_size - 1, (1,)).item()
            line_end_x = torch.randint(line_start_x + 1, image_size, (1,)).item()
            line_end_y = line_start_y + 1

        # Generowanie linii pionowej
        elif alignment == 1:
            line_start_x = torch.randint(0, image_size - 1, (1,)).item()
            line_start_y = torch.randint(0, image_size - 1, (1,)).item()
            line_end_x = line_start_x + 1
            line_end_y = torch.randint(line_start_y + 1, image_size, (1,)).item()

        # Ustawianie wartości pikseli linii na 0 (czarny kolor)
        tensor[:, :, line_start_y:line_end_y, line_start_x:line_end_x] = 0

        # Tworzenie siatki wizualizacji z tensora
        grid = vutils.make_grid(tensor, normalize=False)

        if save_file:
            vutils.save_image(grid, "Sample_data/generated_image_" + str(i) + ".png")

        grids.append(grid)
        line_tensor = torch.tensor([line_start_x, line_start_y, line_end_x, line_end_y])
        line_tensors.append(line_tensor)

    line_tensors = torch.stack(line_tensors).float()
    return grids, line_tensors

