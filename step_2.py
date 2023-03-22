import numpy as np

import tensorflow as tf
import keras


def main():
    def house(cost):
        xs = np.array([0, 1, 2, 3, 4, 5])
        ys = np.array([50, 101, 148, 200, 249, 300])
        model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
        model.compile(optimizer='sgd', loss='mean_squared_error')
        model.fit(xs, ys, epochs=600)
        return model.predict(cost)

    prediction = house([7, 5, 3, 1, 10, 12])
    print(prediction)


if __name__ == '__main__':
    main()
