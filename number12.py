#判断奇数偶数
def getNumber(n):
    while True:
        try:
            value = int(input(n))
            if value < 0:
                print("数字必须大于0")
                continue
            return value
        except ValueError:
            print("必须输入一个整数")
def main():
    a = getNumber("请输入一个数字：")
    if a % 2 == 0:
        print("这是一个偶数")
    else:
        print("这是一个奇数")
if __name__ == "__main__":
    main()