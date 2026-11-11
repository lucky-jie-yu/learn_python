#实现最小公倍数
import number23
def main():
    n1 = int(input("请输入第一个数："))
    n2 = int(input("请输入第二个数："))
    v = number23.gcd(n1, n2)
    print( (n1 // v) * (n2 // v) * v)
if __name__ == "__main__":
    main()