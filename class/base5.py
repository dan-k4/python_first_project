# 特殊メソッド:インスタンスにアクセスする際に、特定の処理を実行すると呼び出されるメソッド。
"""
__str__:str(object),print(object)の際に呼び出され、オブジェクトを文字列として返す
__bool__:if文で理論値を返すことができる
__len__:len()実行時に呼び出される
__eq__:==野代に呼び出される
__hash__:文字列をハッシュ値として返す。この関数を定義することで、クラスを辞書として扱うときや、setに要素を入れる際に利用する
__name__:クラスの名前を返す
"""

class Human:
    def __init__(self,name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + self.phone_number

    def __eq__(self,other):
        return(self.name) and (self.phone_number == other.phone_number)

    def __hash__(self):
        return hash(self.name + self.phone_number)

    def __bool__(self):
        return True if self.age >= 20 else False

    def __len__(self):
        return len(self.name)

man = Human('taro', 20, '0801111111')
man2 = Human('taro',18, '0801111111')
man3 = Human('jiro',19, '0801111111')
man_str = str(man)
print(man)

print(man == man2)
print(hash('taro'))
set_man = {man , man2, man3}
for x in set_man:
    print(x)

if man:
    print('man = Ture')
if man2:
    print('man2 = Ture')

print(len(man))
print(len(man2))
