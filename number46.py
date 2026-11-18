#计算列表元素之积
def _mul(arr):
    ans = 1
    for i in arr:
        ans *= i
    return ans

if __name__ == "__main__":
    arr = [1, 2, 3]
    print(_mul(arr))