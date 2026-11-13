#通过导入datetime模块来获取昨天的日期
import datetime
def getYesterday():
    today = datetime.date.today()
    oneDay = datetime.timedelta(days = 1)
    yesterday = today - oneDay
    return yesterday
print(getYesterday())

