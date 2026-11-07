"""if __name__ == "__main__": 的作用"""
"""下面通过两个 Python 文件，演示同一个模块在直接运行和被导入时的区别。"""
def add(a, b):
    return a + b
def mul(a, b):
    return a * b
def main():
    print(add(1, 2))
    print(mul(1, 2))
if __name__ == "__main__":
    main()