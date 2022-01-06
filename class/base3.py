# コンストラクタ（__init__）
# オブジェクトをインスタンス化する際に呼び出されるメソッドをコンストラクタを言う。
# インスタンス作成時に自動的に呼び出される
# クラスのプロパティを初期化する際などに、コンストラクタを利用すると便利


# デストラクタ (__del__)
# インスタンスを削除する際に呼び出される

class SampleClass:
    def __init__(self,msg, name = None): #コンストラクタ
        print('コンストラクタが呼ばれました')
        self.msg = msg # インスタンス変数
        self.name = name # インスタンス変数

    def __del__(self):
        print('デストラクタが呼ばれました')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

var_1 = SampleClass('Hello', 'Dan')
var_1.print_msg()
var_1.print_name()
del var_1

