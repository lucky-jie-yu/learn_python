#从已有数组创建数组
#将列表转换为 ndarray:
import numpy as np
x = [1, 2 ,3]
a1 = np.asarray(x)
print(a1)

print('-----------------------------------')
#将元组转换为 ndarray:
y = (1 ,2, 3)
a2 = np.asarray(y)
print(a2)
#将元组列表转换为ndarray
print('---------------------------------------')
z = [(1, 2, 3), (4 ,5)]
a3 = np.asarray(z, dtype = object)#必须明确告诉 NumPy：“我知道它不规则，请把它当成对象数组处理”。
print(a3) #输出[(1, 2, 3) (4, 5)]
w = [(1, 2, 3), (4, 5, 6)]
a4 = np.asarray(w)
print(a4)#输出
# [[1 2 3]
# [4 5 6]]
print('-------------------------------------------------')
"""
numpy.frombuffer 用于实现动态数组。

numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象。"
"""
str = b"hello world"
a5 = np.frombuffer(str, dtype = 'S1')
print(a5)

print('----------------------------------------------------')
#numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
list1 = range(6)
it = iter(list1)
a6 = np.fromiter(it, dtype = float)
print(a6)
