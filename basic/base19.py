#enumerate関数 配列の中の値とインデックスを同時に取得する
#zip関数：二つの配列の中の値を同時に取得する
#while:whileの中のしきがTureであるうちは処理を実行する

fruits = ['grape', 'pine', 'apple']

for index, value in enumerate(fruits):
    print('index = {}'.format(index))
    print('value = {}'.format(value))

classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Katuo', 'Wakame', 'Tara']
for A, B in zip (classA, classB):
    print('classA student : {}'.format(A))
    print('classB student : {}'.format(B))

count = 0
while count < 10: #countが10より小さい場合は中の処理を実行
    print(count)
    count += 1


