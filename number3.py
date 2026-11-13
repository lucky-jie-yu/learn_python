#方法重写，如果父类方法的功能不能满足你的需求，可以在子类重写父类方法
#类的私有方法：__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods
class Parent:
    def myMethod(self):
        print("This is parent method")

class Child(Parent):
    __age = 25  # 私有属性
    def myMethod(self):
        print("This is child method")

c = Child()
c.myMethod()
# print(c.__age)  #报错,报找不到的错误

print(c._Child__age)  #Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性

"""
单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
"""
