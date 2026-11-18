#移除字符串中的指定位置字符
def _remove(s):
    ans = ""
    pos = int(input("请输入要移除字符的位置："))
    while True:
        if pos <= 0 or pos >= len(s):
            print("位置输入错误")
            pos = int(input("请重新输入要移除字符的位置："))
            continue
        else:
            break
    ans = s[:pos - 1] + s[pos:]
    print(ans)
if __name__ == "__main__":
   s = input("请输入一个字符串:")
   _remove(s)