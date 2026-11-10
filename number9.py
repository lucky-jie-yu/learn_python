#交换变量
def fun(a, b):
    # 另一种方式
   # a, b = b, a
    return b, a
def main():
    a, b = input("请输入2个变量：").split()
    a, b = fun(a, b)
    print(a ,b)
if __name__ == "__main__":
    main()
