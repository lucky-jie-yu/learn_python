#计算n个自然数的立方和
def fun(n):
    ans = 0
    for i in range(1, n + 1):
        ans += (i ** 3)
    return ans
if __name__ == "__main__":
    n = int(input("请输入项数："))
    res = fun(n)
    print(res)