import sys, paths
sys.path.insert(0, paths.module_path)
sys.path.insert(0, paths.data_path)

import mnist_loader
import network

training_data, validation_data, test_data = mnist_loader.load_data_wrapper(paths.data_path)


net=network.Network(784, 32, 32, 10)

def train():
    batch_size = 50
    for i  in range(batch_size, len(training_data), batch_size):
        batch=training_data[i-batch_size: i]
        for x, y in batch:
            net.update_mini_batch(batch)

def test():


if __name__ == "__main__":
    print("training with the mnist data")
    train()
    print("done")

