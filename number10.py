#通过使用if...elif...else语句判断数字是正数、负数或零
n = float(input("请输入一个数字："))
if n > 0:
    print("这是一个正数")
elif n < 0:
    print("这是一个负数")
else:
    print("这是一个零")