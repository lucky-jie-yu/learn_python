#numpy 数据类型 与数据类型对象dtype

"""
定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
"""
import numpy as np
dt = np.dtype([("name", "U10"), ("age", "i8"),("marks", np.float64) ])
student = np.array([("yujie", 25, 99.0), ("yuyang", 23, 100.0), ("yuheng", 19, 150.0)], dtype = dt)
print(dt)
print(student)