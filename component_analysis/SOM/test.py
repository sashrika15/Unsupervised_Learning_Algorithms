from src.plot import plot
from src.soms import train
from src.utils import read_img

import numpy
import matplotlib.pyplot as plt
from minisom import MiniSom

if __name__ == '__main__':
    image, data = read_img('Images/Testing/Image1.jpeg')
    starting_weights, reduced_image, learnt_weights = train(image, data)
    plot(image, reduced_image, starting_weights, learnt_weights)
