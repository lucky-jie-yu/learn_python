#打印非波那契数列
def fun(n):
    a = 0
    b = 1
    list1 = [0, 1]
    if n == 1:
        print(0)
    elif n == 2:
        print("0, 1")
    else:
        for i in range(3, n + 1):
            a, b = b, a + b
            list1.append(b)
    return list1
n = int(input("请输入数列个数："))
ans = fun(n)
print(ans)