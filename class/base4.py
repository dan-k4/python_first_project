# インスタンスメソッド、クラスメソッド、スタティックメソッド
"""
インスタンスメソッドとは、クラスから作成したオブジェクト（インスタンスを用いて呼び出すメソッド）
第一引数にはself必ずつける（作成したインスタンス自信を表している

クラスメソッドとは、クラスをインスタンス化せず実行できるメソッド
第一引数には必ずclsをとる（クラス自身）

スタティックメソッドとは、インスタンスメソッドやクラスメソッドの様にインスタンスやクラスが引数に渡されることはない。
@staticmethodで定義
クラス変数へもインスタンス変数へもアクセスできない
*インスタンスからクラスメソッド、スタティックメソッドを利用することはできる
"""

class Human:

    class_name = 'Human' # クラス変数

    def __init__(self, name, age): #コンストラクタ
        self.name = name
        self.age = age

    def print_name_age(self): # インスタンスメソッド
        print('インスタンスメソッド実行')
        print('name = {}, age = {}'.format(self.name, self.age))

    @classmethod
    def print_class_name(cls, msg): #クラスメソッド
        print('クラスメソッド実行')
        print(cls.class_name)
        print(msg)

    @staticmethod
    def print_msg(msg): #スタティックメソッド
        print('スタティックメソッドを実行')
        print(msg)

# クラスメソッド
Human.print_class_name('こんにちは')

# インスタンスメソッド
man = Human('桜木', 18)
man.print_name_age()
woman = Human('澤野', 17)
woman.print_name_age()

# スタティックメソッド
man.print_msg('hello static')
Human.print_msg('hello static')
