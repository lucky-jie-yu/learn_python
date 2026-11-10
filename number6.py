#计算圆的面积
import math
def getR(r):
    while True:
        try:
            value = float(input(r))
            if value <= 0:
                print("半径必须大于0")
                continue
            return value
        except ValueError:
            print("请输入有效的信息")
def computeArea(r):
    area = math.pi * (r ** 2)
    return area

def main():
    r = getR("请输入圆的半径：")
    area = computeArea(r)
    print(f"圆的的面积为：{area:.2f}")

if __name__ == "__main__":
    main()
