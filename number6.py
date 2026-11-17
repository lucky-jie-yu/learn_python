#numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：
#numpy.arange(start, stop, step, dtype)
import numpy as np
a1 = np.arange(5)
print(a1)
#设置返回类型为float
b1 = np.arange(5, dtype = float)
print(b1)

#设置了起始值、终止值及步长：
c1 = np.arange(10, 20, 2)
print(c1)

print('----------------------------------------------------------')
"""
numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None
"""
a2 = np.linspace(start = 1, stop = 10, num = 10, endpoint = True, dtype = int) #dtype不指定，默认为float
print(a2) #[ 1  2  3  4  5  6  7  8  9 10]
b2 = np.linspace(1, 1, 10)
print(b2) #[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

print('--------------------------------------------------------')
#将 endpoint 设为 false，不包含终止值：
a3 = np.linspace(start = 1, stop = 7, num = 6, retstep = True, endpoint = False)
print(a3)

print('-------------------------------------------------------------')
#numpy.logspace 函数用于创建一个于等比数列。格式如下：

#np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
"""
参数	描述
start	序列的起始值为：base ** start
stop	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
num	要生成的等步长的样本数量，默认为50
endpoint	该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
base	对数 log 的底数。
dtype	ndarray 的数据类型
"""
a4 = np.logspace(1.0, 2.0, num = 10) #从10的一次方到10的二次方
print(a4)
#输出：
"""
[ 10.          12.91549665  16.68100537  21.5443469   27.82559402
  35.93813664  46.41588834  59.94842503  77.42636827 100.        ]
"""
print('-------------------------------------------------')
#将对数底数设置为2
a5 = np.logspace(0, 9, num = 10, base = 2)
print(a5)  #输出[  1.   2.   4.   8.  16.  32.  64. 128. 256. 512.]





