#装饰器是一个函数：它接收一个函数作为参数，并返回一个新的函数（通常是对原函数的增强版本）
"""
装饰器通过 @decorator_name 语法应用在函数或方法定义之前。

Python 还提供了一些内置装饰器，例如 @staticmethod 和 @classmethod。
"""

#装饰器的核心思想是：用一个函数"包装"另一个函数。
def decorator_function(origin_func):
    def wrapper(*args1, **args2):
        print("执行前")
        result = origin_func(*args1, **args2)
        print("执行后")
        return result
    return wrapper
@decorator_function
def target_func():
    print("原函数执行")
target_func()

print("----------------------------------------")
#打印日志
def my_decorator(func):
    def wrapper():
        print("执行前")
        func()
        print("执行后")
    return wrapper

@my_decorator
def target_func2():
    print("hello")

target_func2()

print("------------------------------------------")
#带参数的装饰器,使用 *args1, **args2 可以兼容任意参数函数
def decorator2(func):
    def wrapper(*args1, **args2):
        print("执行前")
        func(*args1, **args2)
        print("执行后")
    return wrapper
@decorator2
def greet(name):
    print(f"hello, {name}")
greet("yujie")

print("-------------------")
#带参数的装饰器进阶，这是"装饰器工厂"，外层函数用于接收参数。
def repeat(num_time):
    def decorator(func):
        def wrapper(*arg1, **arg2):
            for i in range(num_time):
                func(*arg1, **arg2)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"hello, {name}")

greet("yujie")

print("----------------------------------------")
#函数形式的类装饰器
"""类装饰器：它接收一个类，返回一个新的包装类，从而拦截原类实例的方法调用"""
def logClass(cls):
    class wrapper:
        def __init__(self, *aegs, **kwargs):
            self.wrapped = cls(*aegs, **kwargs)

        def __getattr__(self, name) :
            return getattr(self.wrapped, name)
        def display(self):
            print("调用前")
            self.wrapped.display()
            print("调用后")
    return wrapper
@logClass
class Myclass:
    def display(self):
        print("原方法")
obj = Myclass()
obj.display()


print("---------------------------------------------------")
#类形式的类装饰器,实现单例模式
class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Datebse:
    def __init__(self):
        print("初始化")
db1 = Datebse()
db2 = Datebse()
print(db1 is db2)

print("------------------------------------------------------")
#定义内置装饰器
"""
@staticmethod：定义静态方法
@classmethod：定义类方法
@property：将方法变为属性
"""
class myClass:
    @staticmethod
    def static_method():
        print("静态方法")
    @classmethod
    def class_method(cls):
        print(cls._name_)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value




