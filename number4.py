#python正则表达式
#re.match函数
#re.match(pattern, string, flags=0)
import re
str2 = "Cats are smarter than dogs"

match = re.match(r'(.*) are (.*?) .*', str2, re.M | re.I)

if match:
    print(f"match.group() : {match.group()}")
    print(f"match.group(1) : {match.group(1)} ")
    print(f"match.group(2) : {match.group(2)}")
else:
    print("no match")

#re.search(pattern, string, flag = 0),re.search 扫描整个字符串并返回第一个成功的匹配

search = re.search(r'(.*) are (.*?) .*', str2, re.M | re.I)
if search:
    print(f"s.group() : {search.group()}")
    print(f"s.group(1) : {search.group(1)} ")
    print(f"s.group(2) : {search.group(2)}")
else:
    print("no match")

#re模块中的检索和替换
#re 模块提供了re.sub用于替换字符串中的匹配项。
"""
re.sub(pattern, repl, string, count=0, flags=0)
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""
phone = "2004-959-559 # 这是一个国外电话号码"
#删除字符串中的python注释
num = re.sub(r'#.*$', "", phone)
print(num)
#删除非数字(-)的字符串
num2 = re.sub(r'\D',"", num)
print(num2)

def three(matched):
    value = int(matched.group("value"))
    return str(value * 3)
s = 'A23G4HFD567'
print(re.sub(r'(?P<value>\d+)', three, s))



