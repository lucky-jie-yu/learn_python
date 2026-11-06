#with用于管理资源，with 是 Python 中的一个关键字，用于上下文管理协议（Context Management Protocol）。它简化了资源管理代码，特别是那些需要明确释放或清理的资源（如文件、网络连接、数据库连接等）
#传统的文件的操作
file = open("/home/yujie/learn_python/example.txt", "r")
try:
    content = file.read()
finally:
    file.close()
print(content)

#用with对文件进行操作
with open("/home/yujie/learn_python/example.txt", "r") as file:
    content = file.read()
    print(content)
#文件已经自动关闭

print("----------------------------------------------------")
#同时打开多个文件，对文件进行操作
with open("/home/yujie/learn_python/input.txt", "r") as infile, open("/home/yujie/learn_python/output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content)

print("----------------------------------------------------------")
#数据库连接
# import sqlite3
# with sqlite3.connect("database.db") as conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     result = cursor.fetchall()
#连接自动关闭

print("-------------------------------------------------------------")
#创建自定义的上下文管理器
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时：{self.end - self.start}秒")
        return False
with Timer() as timer:
    sum(range(1000000))

print("-------------------------------")
#使用contextlib模块来创建上下文管理器
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

# 使用示例
with tag("h1"):
    print("这是一个标题")
