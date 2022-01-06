
#関数デフォルト値
# 可変長引数：場合に応じてその都度、因数の長さが変わるもの
# 可変超のタプル* *arg1
# 可変長の辞書** **arg2
# 複数の返り値 a,b

def sample(arg1, arg2 = 100):
    print(arg1,arg2)

sample(200,)

def spam(arg1, *arg2):
    print("arg1 = {},arg2 = {}".format(arg1, arg2))
    print(type(arg2))

spam(1,2,3,4,5)

# 可変長引数を複数設定することはできない
def spam_2(arg1, **arg2):
    print('arg1 = {}, arg2 = {}'.format(arg1, arg2))
    print(type(arg2))

spam_2(3, name='taro', age=20)

def spam_3(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)

spam_3(1,2,3,4,5,name ="taro",age = 15)

def sample_2():
    return 1,2

a, b = sample_2()
print(a,b)