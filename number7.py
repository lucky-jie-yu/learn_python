#随机数的生成
#random.random()返回一个介于0.0和1.0之间的随机小数
import random
n1 = random.random()
print(n1)
print("--------------------------------------------------")
#random.random(a,b)返回一个介于a和b之间的整数(包括a和b)
n2 = random.randint(0, 9)
print(n2)

print("-----------------------------------------------------")
#random.choice(sequence)用于从序列中随即选择一个元素
list1 = [1, 2, 3, 4, 5, 6]
n3 = random.choice(list1)
print(n3)

print("-------------------------------------------------------")
#random.shuffle(sequence)用于将序列中的元素进行随机排序
list2 = [2, 5, 1, 6, 4, 3]
random.shuffle(list2)
print(list2)
