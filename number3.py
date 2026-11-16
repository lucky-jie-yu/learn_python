#numpy数组属性
"""
NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度。

一维数组的秩为 1，二维数组的秩为 2，以此类推。

在 NumPy 中，数组的每一个维度称为一个轴（axis），也就是维度（dimensions）。
"""
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
#对每一列求和
print(a.sum(axis=0))
#对每一行求和
print(a.sum(axis=1))

print("--------------------------------------------")
#ndarray.ndim 用于获取数组的维度数量（即数组的轴数），也就是秩。
a1 = np.arange(24)
print(a1.ndim)
#将a1变为3维的
b1 = a1.reshape(2, 3, 4)
print(b1.ndim)
#ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性（秩)
print(f"a1的形状是：{a1.shape}, b1的形状是：{b1.shape}")
#ndarray.shape 也可以用于调整数组大小
c1 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"c1原来的形状：\n{c1}")
c1 = c1.reshape(3, 2)
print(f"c1变化后的形状：\n{c1}")
#ndarray.size 返回数组中元素的总个数，等于 shape 中各个轴上大小的乘积。
print(c1.size)

"""
ndarray.dtype 返回数组中元素的数据类型。
dtype 对象包含类型名和元素位宽等信息，
"""
print(c1.dtype)
c2 = np.array([1.2, 2.5, 6.6])
print(c2.dtype)#输出float64
#也可以显示指定
c3 = np.array([1, 2, 3,], dtype = "f8")
print(c3) #输出[1. 2. 3.]
print(c3.dtype) #输出float64

print("----------------------------------------------------------------")
#ndarray.real 和 ndarray.imag 分别返回数组中每个元素的实部和虚部，主要在元素类型为复数（complex）时使用。
a3 = np.array([[1+2j, 3+4j, 5+6j], [7+8j,9+10j, 11 + 12j]] )
print(a3)
#打印每个数组的实部
print(a3.real)
#虚部
print(a3.imag)

print("-------------------------------------------------------------------------")
#ndarray.itemsize 以字节的形式返回数组中每一个元素的大小
a4 = np.array([1, 2, 3], dtype = 'i4')
print(a4.itemsize)
b4 = np.array([1, 2, 3], dtype = 'f8')
print(b4.itemsize)