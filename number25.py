#实现简单计算器实现
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
if __name__ == "__main__":
    n1 = int(input("请输入第一个数："))
    op = input("请输入操作符：")
    n2 = int(input("请输入第二个数："))
    ans = 0
    if op == '+':
        ans = add(n1, n2)
    elif op == '-':
        ans = sub(n1, n2)
    elif op == '*':
        ans = mul(n1, n2)
    else:
        ans = div(n1, n2)
    print(ans)