import tensorflow as tf
import numpy as np
from PIL import Image

original_image = np.asarray(Image.open('og.bmp'))
background_image = np.asarray(Image.open('bg.bmp'))
foreground_image = np.asarray(Image.open('fg.bmp'))

assert original_image.shape == background_image.shape
assert original_image.shape == foreground_image.shape

positive_examples = foreground_image - original_image
negative_examples = background_image - original_image

x = []
y = []

for i in range(original_image.shape[0]):
    for j in range(original_image.shape[1]):
        if positive_examples[i][j].tolist() != [0,0,0]:
            x.append([i,j,original_image[i][j][0],original_image[i][j][1],original_image[i][j][2]])
            y.append(1)

for i in range(original_image.shape[0]):
    for j in range(original_image.shape[1]):
        if negative_examples[i][j].tolist() != [0,0,0]:
            x.append([i,j,original_image[i][j][0],original_image[i][j][1],original_image[i][j][2]])
            y.append(0)

x_train = []
y_train = np.asarray(y)

for i in range(len(x)):
    print(i, len(x))
    features = []
    for j in range(len(x)):
        features.append(np.exp(-1*np.linalg.norm(np.asarray(x[i]) -np.asarray( x[j]))))
    x_train.append(features)


x_train = np.asarray(x_train)
