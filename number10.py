#numpy迭代数组
"""
NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。

迭代器最基本的任务的可以完成对数组元素的访问
"""
import numpy as np
a1 = np.arange(6).reshape((2, 3))
for i in np.nditer(a1):
    print(i, end=" ")
print()
print('------------------------------------')
a2 = np.arange(6).reshape((2, 3))
for i in np.nditer(a2.T): #a2.T是a2转置
    print(i, end=" ")  #输出0 1 2 3 4 5 ，a2.T只是视图，没有改变数据的底层存储
print()
for i in np.nditer(a2.T.copy(order = 'C')):
    print(i, end=" ") #输出0 3 1 4 2 5 ，先转置，再copy到一个新开辟的存储空间，改变了底层存储方式
"""
底层储存：
【【0, 3】
  【1, 4】
  【2, 5】】
  order = 'C'按行优先访问
"""

