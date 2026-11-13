#使用递归方式生成斐波那契数列
def fun(n):
    if n <= 1:
        return n
    else:
        return fun(n - 1) + fun(n - 2)
if __name__ == "__main__":
    n = int(input("请输入项数："))
    for i in range(0, n ):
        print(fun(i) , end=" ")







