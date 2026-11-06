#迭代器，有两个基本方法，iter()和next()
from email import generator
from idlelib import multicall

list1 = [1, 2, 3, 4]
it = iter(list1) #创建迭代器对象
print(it)
print(next(it)) #输出迭代器下一个元素
#用for遍历迭代器对象
for x in it:
    print(x, end=" ")
print()
print("----------------------------")
#创建一个迭代器
"""
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
"""
class myNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        b = self.a
        self.a += 1
        return b

number = myNumber()
it = iter(number)
print(next(it))
print(next(it))


print("----------------------------------")
#StopIteration异常用于标识迭代的完成
class age:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < 26:
            c = self.a
            self.a += 1
            return c
        else:
            raise StopIteration

myAge = age()
it = iter(myAge)
for i in it:
    print(i)


print("--------------------------------")
#生成器yield
def countN(n):
    while n > 0:
        yield n
        n -= 1

generator = countN(5)
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1

print("---------------------------")
#使用yield生成斐波那契数列,使用了 yield 的函数被称为生成器（generator）
import sys
def fibonacci(n):
    a, b, count = 0, 1, 0
    while count <= n:
        yield a
        a, b = b, a + b
        count += 1

f = fibonacci(10)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()






