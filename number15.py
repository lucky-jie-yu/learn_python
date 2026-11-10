#质数判断
import math


def getNumber(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 1:
                print("必须输入大于1的自然数")
                continue
            return value
        except ValueError:
            print("请输入数字")
def judge(n):
    if n == 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = getNumber("请输入一个数字：")
    if judge(n) == False:
        print(f"{n}不是一个质数")
    else:
        print(f"{n}是一个质数")
if __name__ == "__main__":
    main()