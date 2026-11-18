#判断字符串是否存在子字符串
def judge(origin, substring):
    if origin.find(substring) != -1:
        return True
    return False

if __name__ == "__main__":
    substring = input("请输入字符串：")
    origin = "hello world"
    if judge(origin, substring):
        print("在")
    else:
        print("不在")
