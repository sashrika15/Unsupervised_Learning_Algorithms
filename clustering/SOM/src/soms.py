import numpy as np
from minisom import MiniSom

def train(img, img_data, ):
    som = MiniSom(x=3, y=3, input_len=3, sigma=0.1, learning_rate=0.1)
    som.random_weights_init(img_data)
    starting_weights = som.get_weights().copy().astype('uint8')
    som.train_random(img_data,1250)
    reduced_img = np.zeros(img.shape)
    quantized = som.quantization(img_data)
    for i,q in enumerate(quantized):
        reduced_img[np.unravel_index(i,shape=(img.shape[0],img.shape[1]))] = q
    learnt_weights = som.get_weights().astype('uint8')
    reduced_image = reduced_img.astype('uint8')
    return starting_weights, reduced_image, learnt_weights
