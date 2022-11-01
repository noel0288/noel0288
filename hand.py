Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tensorflow as tf
... import numpy as np
... mnist = tf.keras.datasets.mnist
... (x_train, y_train),(x_test, y_test) = mnist.load_data()
