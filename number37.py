#将列表中的头尾两个元素对调
def dui_diao(arr):
    n = len(arr)
    if n == 0:
        print("数组长度为0")
        return
    arr[0], arr[-1] = arr[-1], arr[0]


if __name__ == "__main__":
    arr = []
    dui_diao(arr)
    print(arr)