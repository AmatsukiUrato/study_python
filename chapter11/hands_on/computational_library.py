# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    a = np.array([0, 1, 2, 3])
    b = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    print(b.ndim)
    print(b.shape)
    print(b.size)
    print(b.dtype)
    print(b)
    print("bを90度回転させる")
    print(b.T)
    plt.plot(b)
    plt.show()

    x = np.random.randn(5000)
    y = np.random.randn(5000)

    plt.plot(x, y, 'o', alpha=0.1)
    plt.show()
