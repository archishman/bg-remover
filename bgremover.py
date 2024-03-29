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
            x.append([256.0 * i / 677.0,256.0 * j/ 677.0,original_image[i][j][0],original_image[i][j][1],original_image[i][j][2]])
            y.append(1)

for i in range(original_image.shape[0]):
    for j in range(original_image.shape[1]):
        if negative_examples[i][j].tolist() != [0,0,0]:
            x.append([i,j,original_image[i][j][0],original_image[i][j][1],original_image[i][j][2]])
            y.append(0)

y_train = tf.convert_to_tensor(np.asarray(y))
x_train = tf.convert_to_tensor(np.asarray(x))

A = tf.matmul(tf.multiply(x_train, x_train), tf.convert_to_tensor(np.ones((5,len(x)))))

B = tf.transpose(A)

C = tf.scalar_mul(2, tf.matmul(x_train, tf.transpose(x_train)))

D = tf.subtract(tf.add(A, B), C)

with tf.Session() as sess:
    print(sess.run(D))