# デコレータ関数
# 関数オブジェクトを引数にとって引数にとった関数に実行時に変更を加える
# デコレータは関数間で、ある処理を共通に利用したい場合によく用いられる

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('*' * 100)
        func(*args,**kwargs)
        print('*' * 100)
    return wrapper

@my_decorator
def func_a(*args,**kwargs):
    print('func_a done')
    print(args)

@my_decorator
def func_b(*args,**kwargs):
    print('func_b done')
    print(args)

func_a(1,2,3)
func_b(1,2,3)

