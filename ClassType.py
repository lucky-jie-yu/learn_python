#类对象支持两种操作：属性引用和实例化,self 代表类的实例，而非类,self 是实例，self.__class__ 是实例所属的类

#类的方法
class Person:
    name = ""
    age = 0
    _weight = 0
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self._weight = weight
    def speak(self):
        print("我叫 %s， 今年 %d 岁， 体重 %dkg" % (self.name, self.age, self._weight))

p = Person("yujie", 25, 45)
p.speak()

#继承
class Student(Person):
    grade = 0
    def __init__(self, name, age, weight, grade):
        Person.__init__(self, name, age, weight)
        self.grade = grade
    def speak(self):
        print("我叫 %s, 今年 %d, 体重 %d kg, 考了 %d 分" %(self.name, self.age, self._weight, self.grade))
s = Student("yujie", 25, 45, 100)
s.speak()

#多继承
class Speaker:
    topic = ""
    name = ""
    def __init__(self,topic, name ):
        self.topic = topic
        self.name = name
    def speak(self):
        print("我叫 %s, 是一名 %s "%(self.name, self.topic))

class Sample(Speaker, Student):
    def __init__(self, name, age, weight, grade, topic):
        Student.__init__(self, name, age, weight, grade)
        Speaker.__init__(self, topic, name)

    def speak(self):
        print("我叫 %s，我是一个 %s" % (self.name, self.topic))

w = Sample("yujie", 25, 45, 100, "演说家") ##方法名同，默认调用的是在括号中参数位置排前父类的方法
w.speak() #输出，我叫 yujie，我是一个 演说家


print("----------------------------------------------------------------")
#运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return "Vector (%d %d)" %(self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(1, 2)
v2 = Vector(3, 6)
print(v1)
print(v2)
v3 = v1 + v2
print(v3)




