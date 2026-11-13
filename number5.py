#re.compile 函数,compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，可以给 match() 、 search() 以及 findall 等函数使用
#语法格式为：
#re.compile(pattern[, flags])
import re
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four', 2, 10)
print(m) # 从'e'的位置开始匹配，没有匹配
n = pattern.match('one12twothree34four',3, 10)
print(n) # 从'1'的位置开始匹配，正好匹配

#findall在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
"""
语法格式为：
findall(string[, pos[, endpos]])
string : 待匹配的字符串。
pos : 可选参数，指定字符串的起始位置，默认为 0。
endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
"""
p = re.compile(r'\d+')
l = p.findall("runoob 123 google 456")
l2 = p.findall('run88oob123google456', 0, 10)
print(l)
print(l2)

d = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(d)


#re.finditer,和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回,re.finditer(pattern, string, flags=0)
it = re.finditer(r'\d+', "12a32bc43jf3")
for match in it:
    print(match.group())

