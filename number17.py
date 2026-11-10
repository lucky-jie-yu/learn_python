#计算整数的阶乘
n = int(input("请输入一个自然数："))
sum = 1
for i in range(1, n + 1):
    sum *= i
print(sum)