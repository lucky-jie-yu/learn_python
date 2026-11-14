#移除列表中重复的元素
def setList(prompt):
    n = 0
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                print("必须输入大于0的整数")
                continue
            else:
                break
        except ValueError:
            print("必须输入数字")
    print(f"请输入列表元素（总共{n}个）：")
    arr = [input() for _ in range(n)]
    print(f"移除前的列表：{arr}")
    # res = list(dict.fromkeys(arr)) 第一种方法（推荐）：#dict.fromkeys,尽量不要边遍历边删除
    seen = set() #第二种方法：使用集合记录该元素是否见过
    ans = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            ans.append(x)
    print(f"移除后的列表：{ans}")

    # print(f"移除后的列表：{res}")

if __name__ == "__main__":
    setList("请输入列表元素个数：")


