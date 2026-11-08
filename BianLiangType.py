#total = 0 # 这是一个全局变量
# 可写函数说明
total = 0
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ",total)
#函数内是局部变量 :  30
#函数外是全局变量 :  0

print("--------------------------------------------------")
"""
Python 中只有模块（module），
类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块
（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，
"""
if True:
    msg = "i am true"
print(msg)
"""
实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。

如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
"""
def test():
    msg2 = "i am msg2"
#print(msg2) 报错

print("--------------------------------")
"""
global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了
"""
num = 0
def fun():
    global num
    print(num)
    num = 100
    print(num)
fun()
print(num)


print("-----------------------------------------")
"""
如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
"""
def fun1():
    num2 =  0
    def func2():
        nonlocal num2
        print(num2)
        num2 = 10
        print(num2)
    func2()
    print(num2)
fun1()

