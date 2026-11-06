#list推导式
#带iif条件
"""
[表达式 for 变量 in 列表]
[out_exp_res for out_exp in input_list]

或者

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
out_exp_res：列表生成元素表达式，可以是有返回值的函数。
for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
if condition：条件语句，可以过滤列表中不符合条件的值。
"""
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_name =[name.upper() for name in names if len(name) > 3]
print(new_name)

#打印 30 以内可以被 3 整除的整数
numer = [n for n in range(30) if n % 3 == 0 ]
print(numer)

print("-----------------------------------------------------")
#dict推导式
"""
{ key_expr: value_expr for value in collection }

或

{ key_expr: value_expr for value in collection if condition }
"""

# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
listdemo = ['Google','Runoob', 'Taobao']
dict1 = {key : len(key) for key in listdemo}
print(dict1)

#提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dict2 = {x : x ** 2 for x in  [2, 4 ,6]}
print(dict2)

print("------------------------------------------")
#set推导式
"""
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""

#计算1， 2, 3的平方数
my_set = {x ** 2 for x in [1, 2, 3]}
print(my_set)
#判断不是 abc 的字母并输出：
s2 = {x for x in "abracadabra" if x not in "abc"}
print(s2)

print("-------------------------------------------")
#tuple推导式(准确来说应该是生成器表达式)
"""
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
"""
#生成一个包含数字 1~9 的元组
t1 = (x for x in range(1, 10))
print(t1)  #返回的是生成器对象<generator object <genexpr> at 0x7bc2d574cf40>
t1 = tuple(t1)       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(t1)
print("------------------------------------------------")
t2 = (y for y in [1, 2])
print(tuple(t2))  # 第一次转换，输出 (1, 2)
print(tuple(t2))  # 第二次转换，输出 () ！！！变成空元组了！