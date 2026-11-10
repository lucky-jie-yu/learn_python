#判断闰年
def getYear(y):
    while True:
        try:
            value = int(input(y))
            if value < 0:
                print("年份必须为正数")
                continue
            return value
        except ValueError:
            print("无效的输入")
def main():
    year = getYear("请输入年份：")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}yes")
    else:
        print(f"{year}no")
if __name__ == "__main__":
    main()