#Numpy创建数组
#numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
import numpy as np
a1 = np.empty([3,2], dtype = int)
print(a1)

print('-------------------------------------')
#创建创建指定大小的数组，数组元素以 0 来填充，np.zeros
#默认为浮点数
a2 = np.zeros(5)
print(a2)
#显示指定为int
b2 = np.zeros((5,), dtype = int)
print(b2)
#指定自定义的类型
c2 = np.zeros((3,2), dtype = [('x' , 'i4'), ('y', 'i4')])
print(c2)
print('-----------------------------------------------------------------')
#创建指定形状的数组，数组元素以 1 来填充
#默认为浮点数
a3 = np.ones(5)
print(a3)
#自定义类型
b3 = np.ones((2 ,2), dtype = int)
print(b3)

print("--------------------------------------------------------------------------")
#numpy.zeros_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充。
a4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a4)
arr = np.zeros_like(a4, order = 'F')
print(arr)
one_arr = np.ones_like(a4)
print(one_arr)