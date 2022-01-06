#raise 例外を返す
# 呼び出し元にメッセージと共に、例外を返すことができる
class MyEception(Exception):
    pass

def devide(a, b):
    if b == 0:
        raise MyEception('0では割り切れまえん')
    else:
        return a/b

try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))