#计算三角形的面积
import math
def getLong(n):
    while True:
        try:
            value = float(input(n))
            if value <= 0:
                print("边长必须为正数")
                continue
            return value
        except ValueError:
            print("请输入有效的边长")

def isSanJiaoXing(a, b ,c):
    flag = True
    if a + b <= c:
        flag = False
    elif a + c <= b:
        flag = False
    elif b + c <= a:
        flag = False
    if not flag:
        print("无法构成三角形，请重新输入三条边的长度")
    return flag

def computeArea(a, b , c):
     p = (a + b + c) / 2
     area = math.sqrt(p * (p -a) * (p - b) * (p - c))
     return area

def main():
    a = getLong("请输入第一条边的长度：")
    b = getLong("请输入第二条边的长度：")
    c = getLong("请输入第三条边的长度：")
    flag = isSanJiaoXing(a, b, c)
    while not flag:
        a = getLong("请输入第一条边的长度：")
        b = getLong("请输入第二条边的长度：")
        c = getLong("请输入第三条边的长度：")
        flag = isSanJiaoXing(a, b, c)
    area = computeArea(a, b, c)
    print(f"三角形的面积是{area:.2f}")

if __name__ == "__main__":
    main()


