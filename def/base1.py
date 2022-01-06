# 関数
# def 関数名():
#     処理

def print_hello():
    print('Hello World')

print_hello()

def num_max(a :int, b :int):
    print('a = {}, b = {}'.format(a,b))
    if a > b:
        return a
    else:
        return b

print(num_max(12, 58))
print(num_max())
