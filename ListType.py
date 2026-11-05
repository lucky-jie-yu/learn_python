#列表的访问，更新，添加，删除
list1 = [1, 2, 3, 4, 5, 6]
print(list1[2])
print(list1[-3:]) #访问倒数第三个个到末尾,从左到右
print(list1[-1:-4:-1]) #访问倒数第一个到倒数第三个，从右到左，负步长
list1[2] = 8 #更新
print(list1[2])
list1.append(7) #末尾添加
print(list1)
del list1[2] #删除第二个元素
print(list1)
print("---------------------")
#嵌套列表
a =[1, 2, 3]
b =[4, 5, 6]
c =[a, b]
print(c)
print(c[0])
print(c[0][1])

print("------------------------")
#列表比较
import operator
x =[1, 2]
y = [2, 3]
z =[2, 3]
print(operator.eq(x, y))
print(operator.eq(y, z))


#常见的列表函数和方法