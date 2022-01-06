"""
”継承”
ある別のクラスからそのクラスの持っている性質を引き継ぐこと。
（例）車というクラスから軽自動車というクラスを新たに作る場合、
軽自動車というクラスには車クラスと同じプロパティ、メソッドを引き継ぐことができる。
この場合、継承元のクラスをスーパークラス。継承先のクラスをサブクラスと言う。

”ポリモーフィズム”
サブクラスを複数作成して、サブクラスごとに同じ名前のメソッドをそれぞれ作成して、処理の中身を変える。
呼び出す際には中身を意識せず実行できる性質のこと。
"""

# クラスの継承
# class クラス名（継承元）:

class Person: #親クラス

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print('hello {}'.format(self.name))

    def say_age(self):
        print('{} year-old'.format(self.age))

class Employee(Person): #Personの機能を継承する
    
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number
    
    def say_number(self):
        print('my number is {}'.format(self.number))

    def greeting(self, msg=None): #オーバライド
        super().greeting()
        print('I\'m employee phote_number = {}'.format(self.number))
    
    # def greeting(self, age): #オーバーロード
    #     print('オーバーロード')

man = Employee('Tonegawa', 45, '08011111111')
man.greeting()
man.say_age()
man.say_number()


