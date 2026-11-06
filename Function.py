#python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象.
#传入不可变对象实例
def change(a):
    print(id(a)) #指向的是同一个对象，即函数传进来的对象
    a = 10
    print(id(a)) #一个新对象
a = 1
print(id(a))
change(a)

print("--------------------------------------------")
#传入可变对象实例
def changeme(myList):
    myList.append([5, 6, 7 ,8])
    print("函数内取值：",myList)
    return
l1 = [1, 2]
changeme(l1)
print("函数外取值：", l1)

print("---------------------------------------------------------")
"""
概念	发生阶段	怎么判断的？	例子
必须参数	定义函数时	括号里写了变量名，但没有给默认值。	def func(name): 这里的 name 就是必须参数。
默认参数	定义函数时	括号里写了变量名，给了默认值（用 = 连接）。	def func(age=18): 这里的 age 是默认参数，调用时可以不传。
位置参数	调用函数时	直接传值，按先后顺序对应。	func("张三")
关键字参数	调用函数时	写成 参数名=值 的形式，按名字对应。	func(name="张三")
"""

#必须参数，传入参数必须和函数声明时一样

#关键字参数，函数使用关键字参数来确定传入的参数值，使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def printInfo(name, age):
    print("名字：", name)
    print("年龄：", age)
    return
printInfo(name = "yuije", age = 25)
printInfo(age = 25, name = "yujie")

print("----------------------------------------")
#不定长参数
"""
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
"""
def func1(arg1, *vartuple):
    print(arg1)
    print(vartuple)
func1(70, 60, 50)
func1(10) #如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量

print("---------------------------------------------")
"""
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
   加了两个星号 ** 的参数会以字典的形式导入
"""
def func2(arg1, **vardict):
    print(arg1)
    print(vardict)

func2(20, name = "yujie", age = 25)

print("---------------------------------------------")
#声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 *，则星号 * 后的参数必须用关键字传入
def func(a, b, *, c):
    print(a)
    print(b)
    print(c)
# func(1, 2, 3) #报错
func(1, 2, c= 3)

print("-----------------------------------------------")
#匿名函数,lambda
x = lambda a : a + 10
print(x(5)) #输出15
#两个函数相加
sum = lambda arg1, arg2 : arg1 + arg2
print(sum(10, 20))

"""
lambda arguments: expression
lambda是 Python 的关键字，用于定义 lambda 函数。
arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
expression 是一个表达式，用于计算并返回函数的结果。
"""
f = lambda : "hellp world"
print(f())