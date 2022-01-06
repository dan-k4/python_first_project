# ジェネレーター関数
# yield
# def 関数名():
#   yield '文字列'
"""メモリ使用量の削減"""

def generater(max):
    print('ジェネレーター作成')
    for n in range(max):
        try:
            x = yield n
            print('x = {}'.format(x))
            print('yield done')
        except ValueError as e:
            print('throw done')


# gen = generater(10)
# for x in gen:
#     print('x = {}'.format(x))

# n = next(gen)
# print('n = {}'.format(n))

# n = next(gen)
# print('n = {}'.format(n))

# send():yieldで停止している箇所に値を送る
# throw():指定した例外が発生して処理が終了させます
# close():ジェネレータを正常終了させます

gen = generater(10)
next(gen)
gen.send(100)
gen.throw(ValueError('Invalid Value'))
gen.close()
next(gen)