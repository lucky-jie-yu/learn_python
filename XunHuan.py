#while case配合使用
count = 0
while count < 5:
    print("count is ", count)
    count += 1
else:
    print("count is ", count)

print("------------------------------")
#for...else使用
#循环执行完毕（即遍历完 iterable 中的所有元素）后，会执行 else 子句中的代码，如果在循环过程中遇到了 break 语句，则会中断循环，此时不会执行 else 子句。
for i in range(6):
    print(i)
else:
    print("This is finally")

print("-------------------------------")
#使用break退出循环不会执行case
a = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]
for i in a:
    if i == 6:
        break
    else:
        print(i)
else:
    print("not found")

#range指定区间
for i in range(3, 9):
    print(i)

#range指定区间和步长，步长可以为负数
for i in range(1, 10, 2):
    print(i)

print("---------------------------------")
#passpass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句
for letter in "abcde":
    if letter == "d":
        pass
        print("执行pass块")
    print("当前字母：" , letter)
print("Good Bye")
