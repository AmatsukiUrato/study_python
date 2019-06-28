# coding:utf-8
import math
import numpy as np
import pandas as pd

if __name__ == "__main__":
    data_set = pd.read_csv("sample_data.csv")
    print("================")
    print(data_set)
    print("================")
    math_list = np.array(data_set.get("数学"))
    literature = np.array(data_set.get("国語"))

    print("平均値,", np.average(math_list))
    print("中央値,", np.median(math_list))

    count = np.bincount(math_list.astype("int32"))
    print("最頻値,", np.argmax(count))
    print("================")
    print("分散,", np.var(math_list))
    print("標準偏差", math.floor(np.std(math_list)))
