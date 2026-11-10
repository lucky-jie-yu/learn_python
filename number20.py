"""
如果一个 n 位正整数等于其各位数字的 n 次方之和，则称该数为阿姆斯特朗数。 例如 1^3 + 5^3 + 3^3 = 153。

1000 以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
程序检测是否为阿姆斯特朗数
"""
def fun(n,count):
    s = 0
    value = n
    while n != 0:
        s += (n % 10) ** count
        n = n // 10
    if s == value:
        return True
    else:
        return False


n = input("请输入一个正整数：")
count = len(n)
m = int(n)
print(fun(m,count))

