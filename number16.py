#通过调用number15输出指定范围内的素数
import number15
left = int(input("输入左边界："))
right = int(input("输入右边界："))
for i in range(left, right + 1):
    if number15.judge(i):
        print(i, end =" ")
print()
print("--------------------------------------")
#埃拉托斯特尼筛法是一种更高效的算法，尤其适用于找出较大范围内的素数
def findAll(end):
    flag = [True] * (end + 1)
    flag[0] = False
    flag[1] = False
    p = 2
    while p * p <= end:
        if flag[p]:
            for i in range(p * p, end + 1, p):
                flag[i] = False
        p += 1
    return [p for p, is_prime in enumerate(flag) if is_prime]

start = int(input("请输入左边界："))
end = int(input("请输入右边界："))
for i in findAll(end):
    if i >= start:
        print(i, end = " ")