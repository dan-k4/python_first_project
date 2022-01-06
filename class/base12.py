# カプセル化の方法２
# @propety, @var.setter

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self): #getter
        print('getter name')
        return self.__name
    
    @property
    def age(self): #getter
        print('getter age')
        return self.__age
    
    @name.setter
    def name(self, name):
        print('setter name')
        self.__name = name
    
    @age.setter
    def age(self, age):
        print('setter age')
        if age < 0:
            print('please enter a valid age')
            return
        self.__age = age

human = Human('Koichi', 22)
human.name = 'Makoto'
print(human.name)
human.age = -1
print(human.age)

