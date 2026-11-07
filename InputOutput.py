"""
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
"""
import math

s = 'hello python'
print(str(s))
print(repr(s))
 #  repr() 函数可以转义字符串中的特殊字符
s2 = "hello python\n"
print(repr(s2))

# repr() 的参数可以是 Python 的任何对象
print(repr(("yujie", 25))) #元组

print("----------------------------------")
#字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
"""
还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
另一个方法 zfill(), 它会在数字的左边填充 
"""
print(repr(1).rjust(2), repr(6).rjust(3))
print('6'.zfill(5))

print("------------------------------------------------------------")
#str.format()的基本使用,括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
print("网址{}: {}".format("菜鸟教程"," https:www.com"))
#在括号中的数字用于指向传入对象在 format() 中的位置
print("{0}, {1}".format("yujie", "yuyang"))
print("{1}, {0}".format("yujie", "yuyang"))


print("-----------------------------------------------------------------")
#如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print("{name}网址 ： URL_{value}".format(name = "菜鸟教程", value = "htttps:www.com"))
#位置及关键字参数可以任意的结合
print("age: {1}, name: {0}, sex: {sex}".format("yujie", "25", sex = "boy"))

print("---------------------------------------------------------------------")
#可选项 : 和格式标识符可以跟着字段名
print("pi后面保留3位小数:{0:.3f}".format(math.pi))
#在 : 后传入一个整数, 可以保证该域至少有这么多的宽度
print("数字保留6个宽度{0:5}{1}".format("6", "9"))

print("-----------------------------------------------------------------------")
"""
如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值
"""
table = {"google" : 1, "baidu" : 2, "edge" : 3}
print("baidu: {0[baidu]:d}; edge: {0[edge]:d}; google: {0[google]:d}".format(table))

print("-----------------------------------------------------------------------------")
#% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串.
print("常数值pi是:%5.3f" %math.pi)


print("-------------------------------------------------------------------------")
"""
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对
"""
import pickle
datal = {"a" : [1, 2.0, 3, 4+6j],
         "b" : {"string", u"Unicode string"},
         "c" : None
         }
self_list = [1, 2, 3, 4]
self_list.append(self_list) #列表包含了对自身的引用，形成循环结构
"""普通文本格式（如 JSON）遇到这种循环引用会无限递归、直接失败。pickle 能正确处理循环引用，读回来仍然是"自己引用自己"的结构，这是 pickle 的一大优势"""
print(self_list)
output = open("data.pkl", "wb") #必须用 'wb'，不能用 'w'。pickle 输出的是字节流，文本模式会破坏字节
pickle.dump(datal,output) #将datal以二进制形式写入output,协议是0
pickle.dump(self_list, output, -1) #将self_list写入文件，-1表示使用python支持的最高协议
output.close()
print("-----------------------------------------------------")
#将之前写入的读出来
with open("data.pkl", "rb") as f:
    data_loaded = pickle.load(f) #读出第一个对象
    self_list_loaded = pickle.load(f) #读出第二个对象
print(data_loaded)
print(self_list_loaded)
print(self_list_loaded[4] is self_list_loaded)

