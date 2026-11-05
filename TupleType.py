#创建空元组
tuple()
#创建只含一个元素的元组
tuple1 = (5,)
print(type(tuple1)) #类型是tuple
tuple2 = (5)
print(type(tuple2)) #类型是int

print("-------------------------")
#元组元素不能修改，但可以拼接
t1 = (1, 2, 3)
t2 = ("a", "b", "c")

t3 = t1 + t2
print(t3)
t2 += t1
print(t2)

#删除元组
del t1
#报错print(t1)

#元组内置函数，tuple(iterable),将可迭代系列转换为元组
list1 = [1, 2, 3, 4, 5]
t2 = tuple(list1)
print(t2)
