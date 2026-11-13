"""
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""
class Employee:
    '所有员工的基类'
    employCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employCount += 1
    def displayEmployeeInfo(self):
        print(f"name is {self.name}, salary is {self.salary}")

    def displayEmployeeCount(self):
        print(f"员工的数量是：{Employee.employCount}")

if __name__ == "__main__":
    e1 = Employee("yujie", 50000)
    e2 = Employee("yuyang", 50000)
    e1.displayEmployeeInfo()
    e2.displayEmployeeInfo()
    e1.displayEmployeeCount()
    e2.displayEmployeeCount()
    Employee.displayEmployeeCount(e1)
    hasattr(e1, "age")
    # getattr(e1, "age")
    setattr(e1, "age", 23)
    print(getattr(e1, "age"))
    print(hasattr(e1, "age"))
    delattr(e1, "age")
    print(hasattr(e1, "age"))
    print(id(e1), id(e2))
    del e1
    del e2
"""
你也可以使用以下函数的方式来访问属性：
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
"""

#析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行

