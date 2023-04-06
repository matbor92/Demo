import random
import csv

random.seed(1234)

def generate_data(filename, num_examples):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for i in range(num_examples):
            features = []
            for j in range(39):
                if j < 3 or random.randint(0, 1):
                    features.append(random.randint(0, 100))
                else:
                    features.append(round(random.uniform(0, 10000), 4))
            label = random.randint(0, 1)
            features.append(label)
            writer.writerow(features)

generate_data('data.csv', 10000)