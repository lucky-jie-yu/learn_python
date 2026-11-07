#用列表实现栈
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return IndexError("pop from an empty stack")
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return IndexError("top from an empty stack")
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("栈顶元素：", stack.top())
print("栈大小：", stack.size())

print("----------------------------------------------------")
"""
Python 提供了 collections.deque，它是双端队列，可以在两端高效地添加和删除元素,使用 collections.deque 实现队列
"""
from collections import deque
queue = deque() #创建一个空队列

#向队尾添加元素
queue.append(1)
queue.append(2)
queue.append(3)
print("状态队列：", queue)
first_num = queue.popleft() #从队首移除元素
print(first_num)
print("队列状态：", queue)
print(queue[0]) #查看队首元素
print(len(queue)) #获取队列大小

