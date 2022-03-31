import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow import keras

np.random.seed(42)

fashion_mnist = keras.datasets.fashion_mnist
(x_train,y_train),(x_test, y_test) = fashion_mnist.load_data()
print(x_train.shape,x_test.shape)

x_train = x_train/255.0
x_test = x_test/255.0

plt.imshow(x_train[1], cmap ='binary')
plt.show()

np.unique(y_test)

class_name = ['T-shirt/Top','Trouser','Pullover','Dress','Cost','Sandal','Shirt','Sneaker','Bag','Ankle Boot']
n_rows = 5
n_cols = 10

plt.figure(figsize=(n_cols * 1.4, n_rows * 1.6))

for row in range(n_rows):
    for col in range(n_cols):
        index = n_cols * row + col
        plt.subplot(n_rows, n_cols,index + 1)
        plt.imshow(x_train[index], cmap='binary', interpolation='nearest')
        plt.axis('off')
        plt.title(class_name[y_train[index]])

plt.show()

model_CNN = keras.models.Sequential()

model_CNN.add(keras.layers.Conv2D(filters=32, kernel_size = 7,padding='same', activation='relu', input_shape=[28, 28, 1]))
model_CNN.add(keras.layers.MaxPooling2D(pool_size= 2))

model_CNN.add(keras.layers.Conv2D(filters=64, kernel_size = 3,padding='same', activation='relu'))
model_CNN.add(keras.layers.MaxPooling2D(pool_size= 2))

model_CNN.add(keras.layers.Conv2D(filters=32, kernel_size = 3,padding='same', activation='relu'))
model_CNN.add(keras.layers.MaxPooling2D(pool_size= 2))

model_CNN.summary()

model_CNN.add(keras.layers.Flatten())
model_CNN.add(keras.layers.Dense(units=128,activation='relu'))
model_CNN.add(keras.layers.Dense(units=64,activation='relu'))
model_CNN.add(keras.layers.Dense(units=10,activation='softmax'))

model_CNN.summary()

model_CNN.compile(loss='sparse_categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

x_train = x_train[...,np.newaxis]
x_test = x_test[...,np.newaxis]

history_CNN = model_CNN.fit(x_train, y_train, epochs=2,validation_split=0.1)
pd.DataFrame(history_CNN.history).plot()
plt.grid(True)
plt.xlabel('epochs')
plt.ylabel('loss/accuracy')
plt.title('Training and Validation plot')
plt.show()
test_loss, test_accuracy = model_CNN.evaluate(x_test, y_test)

print('Test Loss : {},Test Accuracy : {}'.format(test_loss, test_accuracy))