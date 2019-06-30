import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data_set = pd.read_csv("sample_data.csv")
print("================")
print(data_set)
print(type(data_set))
print("================")

math_list = np.array(data_set.get("数学"))
literature = np.array(data_set.get("国語"))

ave = math.floor(np.average(math_list))
med = math.floor(np.median(math_list))
count = np.bincount(math_list.astype("int32"))
arg = np.argmax(count)
var = math.floor(np.var(math_list))
std = math.floor(np.std(math_list))

print(ave, med, arg, var, std)
plot_arr = np.array([ave, med, arg, std])

plt.annotate("hoge", xy=(4.5, ave + 3))
plt.scatter(np.array([1, 2, 3, 4]), plot_arr, c='red')
plt.scatter(np.array([5]), ave, c='green')
plt.scatter(np.array([0, 0, 0, 0, 0]), math_list, c='blue')
plt.show()
