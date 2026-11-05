string = "123456789"

print(string)#输出字符串
print(string[0:-1])#输出第一个字符到倒数第二个字符，左闭右开
print(string[0:1])#输出字符串的第一个字符
print(string[0])#输出字符串第一个字符
print(string[2:5])#输出从第三个开始到第六个的字符（不包含）
print(string[2:9])# 输出从第三个开始后的所有字符
print(string[2:]) # 输出从第三个开始后的所有字符
print(string[1:5:2])# 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(string * 2)# 输出字符串两次
print(string + "nihao")  # 连接字符串

print("-------------")
print("hello\nrunoob" )  # 使用反斜杠(\)+n转义特殊字符
print(r"hello\nrunoob")   # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


