#复制列表
def copy(arr):
    l = []
    for i in arr:
        l.append(i)
    return l
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5 ,6]
    new_arr =copy(arr)
    print(new_arr)