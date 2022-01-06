"""
継承とポリモーフィズムを用いた演習です。

Dogクラスを作成して:speakメソッドを実行すると「ワン」と表示します
Catクラスを作成して:speakメソッドを実行すると「にゃー」と表示します
Sheepクラスを作成して:speakメソッドを実行すると「メー」と表示します
Otherクラスを作成して:speakメソッドを実行すると「その動物は存在していません」と表示します

ユーザーからの入力を受け付け
１の場合はDogクラスのSpeakメソッドを
２の場合はCatクラスのSpeakメソッドを
３の場合はSheepクラスのSpeakメソッドを
それ以外はOtherクラスのSpeakメソッドを実行します。
"""

from abc import abstractmethod, ABCMeta

class Animals(metaclass = ABCMeta):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animals):
    def speak(self):
        print('wan')

class Cat(Animals):
    def speak(self):
        print('nya-')

class Sheep(Animals):
    def speak(self):
        print('me-')

class Other(Animals):
    def speak(self):
        print('その動物は存在しません')

number = input('which animals do you like? 1:dog, 2:cat, 3:sheep')
if number == '1':
    animal = Dog()
elif number == '2':
    animal = Cat()
elif number == '3':
    animal = Sheep()
else:
    animal = Other()

animal.speak() # speak (ポリモーフィズム)