
#
# #适合正数
# n1 = float(input("请输入一个数："))
# res = n1 ** 0.5
# print(f"{n1} 的平方根是 {res : .2f}")

print("-------------------------------")
#负数和复数可以使用以下的方式
import cmath
n2 = complex(input("请输入一个数："))  #如果是负数，则用float
ans = cmath.sqrt(n2)
print(f"{n2}的平方根是{ans.real:.2f}+{ans.imag:.2f}j")



