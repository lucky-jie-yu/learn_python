#使用正则表达式提取字符串中的URL
import re
def _findAll(string):
    url = re.findall(r'https?://(?:[\w.-]|(?:%[\da-fA-F]{2}))+', string)
    return url


string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", _findAll(string))