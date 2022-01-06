# inner関数とノンローカル関数
# inner関数:関数の内部に関数を書くことができる
# inner関数外の関数の外からアクセスできないような関数を作成する
# 関数の中で同じ処理が難度も発生する場合に、一つにまとめる
# ノンローカル関数

def outer():
    outer_value = '外側の変数'
    def inner():
        nonlocal outer_value
        outer_value = '内側の変数'
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    inner()
    print('outer : outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

# inner() #関数の外なので呼び出せない
outer()

