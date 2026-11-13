#数组翻转指定个数的元素
def _reverse(arr, d, n):
    if n == 0:
        return
    if d > n:
        print("d不能大于n")
        return
    m = d % n
    if m == 0:
        return
    count = 0
    while True:
        arr.append(arr.pop(0))
        count += 1
        if count == m:
            break
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6 ,7]
    d = 2
    n = len(arr)
    _reverse(arr, d, n)
    print(arr)