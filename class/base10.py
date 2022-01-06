# Private 変数
# インスタンス変数は外部からアクセスして値を書き換えられる。
# アクセスのできない変数を定義する必要がある
# アンダースコアを二つつけて定義(__)

class Human:
    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name # private
        self.age = age

    def print_msg(self):
        print('name = {}, age = {}'.format(self.__name, self.age))

human = Human('Taro', 15)
print(human.__name)
human.print_msg()



