#摄氏温度转华氏温度
def getTemper(t):
    while True:
        try:
            return float(input(t))
        except ValueError:
            print("无效的输入")
def fun(t):
    res = t * 1.8 + 32
    return res
def main():
    t = getTemper("请输入摄氏温度：")
    ans = fun(t)
    print(f"华氏温度是{ans:.2f}")
if __name__ == "__main__":
    main()