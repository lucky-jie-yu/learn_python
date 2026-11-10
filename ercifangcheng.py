#二次方程
import cmath


def getFloat(n):
    while True:
        try:
            return float(input(n))
        except ValueError:
            print("请输入有效的信息")

def getRoot(a, b, c):
    value = b ** 2 - 4 * a * c
    root1 = ((-b) + cmath.sqrt(value)) / (2 * a)
    root2 = ((-b) - cmath.sqrt(value)) / (2 * a)
    return root1, root2

def main():
    a = getFloat("请输入二次项系数a(a != 0):")
    while a == 0:
        print("a 不能等于0")
        a = getFloat("清重新输入二次项系数a(a != 0):")
    b = getFloat("请输入一次项系数b:")
    c = getFloat("请输入常数项系数c:")
    root1, root2 = getRoot(a, b, c)
    print(f"方程的解是{root1}和{root2}")

if __name__ == "__main__":
    main()






