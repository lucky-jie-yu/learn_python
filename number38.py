#将列表中的指定位置的两个元素对调
def _swap(arr, pos1, pos2):
    l = len(arr)
    if pos1 < 0 or pos2 < 0:
        print("位置输入不合法")
        return
    elif pos1 >= l or pos2 >= l:
        print("位置输入不合法")
        return
    else:
        arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
        return
if __name__ == "__main__":
    pos1 = int(input("请输入第一个位置："))
    pos2 = int(input("请输入第二个位置："))
    my_list = [23, 65, 19, 90]
    print(my_list)
    _swap(my_list, pos1, pos2)
    print(my_list)