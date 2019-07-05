# -*- coding: UTF-8 -*-

import math
import numpy as np
import pandas as pd


def calc_statistics_from_csv():
    data_set = pd.read_csv("sample_data.csv")
    print(data_set)
    print("================")
    np_math = np.array(data_set.get("数学"))
    np_literature = np.array(data_set.get("国語"))

    math_statistics_list = create_statistics(np_math)
    literature_statistics_list = create_statistics(np_literature)

    print(type(math_statistics_list))
    print(type(literature_statistics_list))

    label_list = ["平均値", "中央値", "最頻値", "分散", "標準偏差"]
    math_dict = dict(zip(label_list, map(str, math_statistics_list)))
    literature_dict = dict(zip(label_list, map(str, literature_statistics_list)))
    statistics = {"数学": math_dict, "国語": literature_dict}
    return statistics


def create_statistics(np_list):
    ave = math.floor(np.average(np_list))
    med = math.floor(np.median(np_list))
    count = np.bincount(np_list.astype("int32"))
    arg = np.argmax(count)
    var = math.floor(np.var(np_list))
    std = math.floor(np.std(np_list))
    return [ave, med, arg, var, std]


if __name__ == "__main__":
    calc_statistics_from_csv()
