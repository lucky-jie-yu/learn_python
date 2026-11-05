import inspect

#int()强制类型转换
from doctest import DocFileSuite

a = int(1)
b = int(2.5)
c = int("3")
print(a)
print(b)
print(c)

print("-----------")
#float()强制类型转转
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

print("------------")
#str()强制类型转换
j = str("s1")
k = str(1)
l = str(2.5)
print(j)
print(k)
print(l)

print("--------------")
#测试强制类型转换
num_int = 123
num_str = "456"
print(type(num_int))  #打印num_int的类型
print(type(num_str))  #打印num_str的类型

num_str = int(num_str) #强制转换成int
print(type(num_str))

num_sum = num_str + num_int
print(type(num_sum))
print(num_sum)


print("------------------")
#Docstring文档字符串
def add(a, b):
    "这个是实现两数相加的函数"
    return a + b
help(add) #使用help函数查看文档说明
print(add.__doc__) #通过_doc_属性访问

print(inspect.getdoc(add)) # 使用 inspect.getdoc() 获取文档

print("----------------------")
#多行Docstring
def calculate(a, b, op = "add"):
    """
    a 是第一个参数
    b 是第二个参数
    op 是具体操作
    ‘’‘

    :param a:
    :param b:
    :param op:
    :return:
    """
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return a / b
    else:
        raise ValueError("不支持的操作")

help(calculate)  #查看完整文档

print("---------------------------")
#Docstring 用于类
class Person:
    """人物类用于表示一个人的基本信息"""
    def __int__(self, name, age):
        """初始化人物信息
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def introduce(self):
        """介绍这个人"""
        return f"我叫{self.name},今年{self.age}岁"

print(Person.__doc__) #访问类的文档
print(Person.introduce.__doc__) #访问方法的文档

print("--------------------------------------")
#海象运算符的使用
my_list = [1, 2, 3]
if (n := len(my_list)) > 2:
    print(f"列表长度为{n}")

print("-----------------------")
#与或非运算
a = 60
b = 13
c = 0

c = a & b #位运算
print("与运算c的值为：",c)

c = a | b #或运算
print("或运算c的值为：",c)

c = a ^ b #异或运算
print("异或运算c的值为：", c)

c = ~a #取反运算
print("取反运算c的值为：", c)

c = a << 2  #左移两位
print("左移两位的值为：", c)

c = a >> 2  #右移两位
print("右移两位的值为：", c)

print("--------------------------")
#逻辑运算,重点看print里的运算规则
a, b = 10, 20
if(a and b):
    print("a为False,返回a,否则返回b, 返回：a")
else:
    print("返回b")
if(a or b):
    print("a为True,返回a，否则返回b, 返回：b")
else:
    print("返回a")
if(not a):
    print("a为True,返回False")
else:
    print("a为False,返回True")

print("-----------------------------------")
#python成员运算符， in， not in
a, b = 1 ,20
my_list = [1, 2, 3, 4, 5]
if a in my_list:
    print("a 在列表中")
else:
    print("a 不在列表中")

if(b not in my_list):
    print("b 不在列表中")
else:
    print("b 在列表中")

print("-------------------------")
#python身份运算符，is ,is not, is用于判断两个变量引用对象是否为同一个
a, b = 20, 30
if(a is b):
    print("a与b有相同的标识")
else:
    print("a与b没有相同标识")

if(id(a) == id(b)): # id() 函数用于获取对象内存地址
    print("a与b有相同的标识")
else:
    print("a与b没有相同的标识")
a = 30
if (a is b):
    print("a与b有相同的标识")
else:
    print("a与b没有相同标识")

if (id(a) == id(b)):
    print("a与b有相同的标识")
else:
    print("a与b没有相同的标识")