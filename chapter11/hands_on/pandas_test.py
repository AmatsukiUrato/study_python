# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset1 = pd.read_csv("sample_dataset.csv")
print(dataset1)
print("=============")
print("=============")
print("=============")

b = np.array(dataset1.get("Salary"))

plt.plot(b, 'o', alpha=1)
plt.show()
