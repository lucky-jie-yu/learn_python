

a =  b = c = 1  #同时为多个变量赋值
print(a)
print(b)
print(c)
print("-------------------------")
x, y, z , u= 1, 2.0, "hello" , 2+3j#为多个变量连续赋值
print(x)
print(y)
print(z)
print(u)
print(type(x))
print(type(y))
print(type(z))
print(type(u))

print("---------------------")
#列表
my_list = [1, 2.0, "hello", 2+3j]
tiny_list = ["123", "hello", 2.0]
print(my_list)  # 打印整个列表
print(my_list[0])  # 打印第一个元素（索引 0)
print(my_list[1:3])   # 打印索引 1 和 2 的元素（不含索引 3）
print(my_list[2:])  # 打印从索引 2 开始到末尾的所有元素
print(tiny_list * 2) # 重复打印 tinylist 两次
print(my_list + tiny_list) # 拼接两个列表


print("-----------------------")
#元组
my_tuple =(1, 2.0, "hello", 2+3j)
tiny_tuple = ("123", "hello", 2.0)
print(my_tuple) #打印整个元组
print(my_tuple[0]) #输出第一个元素
print(my_tuple[1 : 3]) #输出索引1和2的元素
print(my_tuple[2 :]) #输出从索引2开始的所有元素
print(tiny_tuple * 2) #连续输出两次tinytuple
print(my_tuple + tiny_tuple) #连接2个元组

print("-------------------")
#集合
my_set = {1, 2.0, "hello", 2+3j, "hello"}
print(my_set)
#成员测试
if "hello" in my_set:
    print("hello在集合中")
else:
    print("hello不在集合中")

#set进行集合运算
a = set("aabc")
b = set("bcd")
print(a) #a只打印一次
print(a - b) #差集
print(a & b) #交集
print(a | b) #并集
print(a ^ b) #对称差集（在 a 或 b 中，但不同时存在）

print("------------")
#字典
my_dict = {}
my_dict["a"] = 1
my_dict["b"] = 2
my_dict["c"] = 3
tiny_dict = {"name" : "runoob", 'code' : 1, 'site' : 'www.runoob.com'}
print(my_dict["a"]) #输出键为a的值
print(my_dict['b']) #输出键为b的值
print(my_dict) #输出完整的字典
print(tiny_dict.keys()) #输出所有的建
print(tiny_dict.values()) #输出所有的值
print("---------------")
#bytes类型

w = b"hello"
print(w)
print(type(w))
print(w[0])

#bytes切片，拼接，查找..
f = w[1:3]
print(f)
print(w + b"world")

#bytes类型中的元素是整数值，进行比较操作要用整数值，ord函数将字符转成对应的整数值
if w[0] == ord('h'):
    print("第一个元素是h")




