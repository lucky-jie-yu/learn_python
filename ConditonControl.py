#match case 匹配
def http_error(status):
    match status:
        case 200:
            return "ok"
        case 404 | 403: #一个case也可以放多个匹配条件
            return "not found"
        case 400:
            return "bad request"
        case _:  #类似与c的default
            return "error"


print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(200))
print(http_error(403))