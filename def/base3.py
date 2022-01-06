#グローバル変数

def printAnimal():
    global animal
    animal = 'cat'
    print('関数内Animal = {}, id = {}'.format(animal,id(animal)))

animal = 'dog'
printAnimal()
print('関数外Animal = {}, id = {}'.format(animal,id(animal)))




