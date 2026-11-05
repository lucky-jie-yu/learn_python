import time


#string的访问与截取
s1 = "hello"
print("s1的第一个字符是：",s1[0])
print("s1的第二个-第五个字符", s1[1:5])

#字符串更新
print("已更新字符串：", s1[:3] + "_word")

#模拟进度条
for i in range(101):
    bar = "[" + "=" * (i // 2) + " " * (50 - i // 2) + "]"
    print(f"\r{bar} {i : 3}%", end="", flush=True)
    time.sleep(0.05)
print()
print("----------------------------------")
#字符串格式化
print("我叫 %s, 今年 %d 岁" %("yujie",25))
print("------------------------------------")
#python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
s2 = '''这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]'''
print(s2)

#f-string
name = "yujie"
print(f"hello {name}")

#使用 = 符号来拼接运算表达式与结果
x = 1
print(f"{x + 1 =}")