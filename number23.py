#最大公约数算法
def getN(prompt):
    while True:
         try:
             val = int(input(prompt))
             if val <= 0:
                 print("必须输入正整数")
                 continue
             return val
         except ValueError:
             print("无效的输入")
def gcd(n1, n2):
    while n1 != 0 and n2 != 0:
        m1 = max(n1, n2)
        m2 = min(n1, n2)
        n1, n2 = m2, m1%m2
    return max(n1, n2)

n1 = int(input("请输入第一个数："))
n2 = int(input("请输入第二个数："))
print(gcd(n1, n2))