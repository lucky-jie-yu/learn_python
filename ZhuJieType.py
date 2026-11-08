#变量注解
name : str = "yujie"
age :int = 25
is_student : bool = True
score : list = [100, 95, 90]

#函数注解
def greet(firstname : str, lastname : str) -> str:
    full_name = firstname + lastname
    return full_name
my_name = greet("yu", "jie")
print(my_name)

print("-------------------------------------------------------")
#参数默认值,可以同时使用类型注解和默认值
def say_hello(name : str, time : int = 1):
    for i in range(time):
        print(name)
say_hello("Bob")
say_hello("yujie", 3)


print("------------------------------------------------------------")
#复杂类型注解，列表，字典容器等，用Python 的 typing 模块提供更强大的工具
from typing import List, Set, Tuple, Dict
# List[int] 表示这是一个只包含整数的列表
numbers : List[int] = [1, 2, 3]
# Dict[str, int] 表示这是一个键为字符串、值为整数的字典
numbers2 : Set[float] = {1.5, 2.5, 1.5, 6.6}
# Tuple[int, str, bool] 表示这是一个包含整数、字符串、布尔值的元组
person : Dict[str, int] = {"yujie" : 25, "yuyang" : 23}
# Set[str] 表示这是一个只包含字符串的集合
person_info :  Tuple[str, int, str] = ("yujie", 25, "boy")

print("---------------------------------------------------------------")
"""
可选类型（Optional）
当值可能是某种类型或者是 None 时使用
"""
from typing import Optional
def find_student(name : str) -> Optional[str]:
    "根据学生查找名字，也可能为None"
    student = {"yujie" : 1, "yuyang" : 2}
    return student.get(name)


print("-------------------------------------------------------------")
#联合类型（Union）,当值可能是多种类型时使用
from typing import Union
def process_input(data : Union[str, int, List[int]]) -> None:
    """处理可能是字符串、整数或整数列表的输入"""
    if isinstance(data, str):
        print(f"data is {data}")

    if isinstance(data, int):
        print(f"data is {data}")

    if isinstance(data, list):
        print(f"data is {data}")
process_input("yujie")
process_input(100)
process_input([1, 2, 3, 4, 5, 6])


print("-----------------------------------------------------------------")
#综合案例
from typing import List, Dict, Set, Union, Tuple,Optional
def compute_average_score(students: List[Dict[str, Union[str, int]]]) -> Optional[float]:
    if not students:
        return None
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)

students_data = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie", "score": 92}
]

aver = compute_average_score(students_data)
print("平均分是{:.2f}".format(aver))
print(f"平均分是{aver:.2f}")
