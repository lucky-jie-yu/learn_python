#判断元素是否在列表中
def judge(arr, n):
    flag = True
    if n not in arr:
        flag = False
    return flag
if __name__ == "__main__":
    arr = [1, 2, 3 ,4 ,5, 6]
    n = int(input("请输入要判断的数："))
    print(judge(arr, n))
