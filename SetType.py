#创建空集合
s1 = set()
print(s1)
print("-----------------------------")
#使用大括号 {} 创建非空集合，元素之间使用逗号分隔，也可以使用 set() 从可迭代对象创建集合
s2 = {1, 2, 2, 3} #使用大括号创建集合
s3 = set([4, 5, 6]) #从列表创建集合
s4 = set("hello") #从字符串创建集合,自动去重
print(sorted(s2))
print(sorted(s3))
print(sorted(s4))

print("-------------------------")
#集合运算，交，并，补，差
a = {1, 2, 3}
b = {3, 4, 5}
print(sorted(a | b)) #并
print(sorted(a & b)) #交
print(sorted(a - b)) #差
print(sorted(b - a)) #差
print(sorted(a ^ b)) #对称差集
print("------------------")
#使用方法，返回一个新的集合，不直接修改原集合
c = a.union(b)  #并
d = a.intersection(b) #交
e = a.difference(b) #差
f = a.symmetric_difference(b) #对称差
print(c)
print(d)
print(e)
print(f)
print("--------------------------")
#集合推导式
square = {x * x for x in range(1, 6)}
print(square)
#过滤字符串中的指定字符
letters = {
    x for x in "abracadabra"
    if x not in "abc"
}
print(sorted(letters))
print("---------------------------")
#🕸集合中添加一个和多个元素
a = {1, 2}
a.add(3) #增加一个
a.add(3) #重复不会报错
a.update({4, 5}) #添加多个
print(a)
print("---------------------")
#如果向 update() 传入字典，添加的是字典的键，而不是值
a.update({"name":"yujie"}, {"age", 25})
print(a)

#删除元素，remove(x)（删除不存在的抛异常）,discard(x)（删除不存在的抛异常）,pop(),pop()随机删除

print("----------------------------------------")
#判断子集，超集，不相交集
a = {1, 2, 3, 4, 5, 6}
b = {2, 5, 6}
print(a.issubset(b)) #判断a
c = {6, 7}# 是否是b的子集
print(b.issubset(a))  #判断b是否是a的子集
print(a.issuperset(b))  #判断a是否是b的超集
print(b.isdisjoint(a))  #判断两个集合是否没有公共元素
print("-------------------------------------")
#也可以使用比较运算符
print(a <= b) #子集
print(a < b) #真子集
print(a >= b) #超集

print("------------------------------")
#不可变集合frozenset
a = frozenset({2, 1, 3, 4})
print(sorted(a))
print(type(a))
b = frozenset([7, 9, 5])
print(a | b)
print(a & b)

#由于 frozenset 本身可以作为可哈希对象使用，因此也可以将它作为其他集合的元素
c = {frozenset([1, 2]), frozenset([3, 4]), frozenset([5, 6])}
print(len(c))





