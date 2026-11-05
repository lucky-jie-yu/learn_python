#创建空字典
d1 = {} #空字典
print(d1)
print("d1的数量", len(d1))
print(type(d1))
d2 = dict() #使用dict内建函数创建空字典

print("--------------------------------")
#向字典中增加，修改，删除
d3 = {"name" : "yujie", "age" : 25}
print(d3)
d3["name"] = "xinyuncao"
d3["career"] = "student"
print(d3)
del d3["career"]
# 报错 print(d3["career"])

print("----------------------------------------")

#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
d4 = {"name" : "yujie", "age" : 24, "age" : 25}
print(d4)

#键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，
#报错d5 = {[1] : 1}
