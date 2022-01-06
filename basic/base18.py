#ループ文 for, while

for i in range(10):
    print(i)

#ループさせるだけの処理
for _ in range (100):
    print('A')

for i in range (2, 20, 3):
    print(i)

sample = ['John', 'Paul', 'George', 'Ringo']
for member in sample:
    print(member)

sample = ('John', 'Paul', 'George', 'Ringo')
for member in sample:
    print(member)

human = {
    'name': 'taro',
    'age':20,
    'gender':'male'
}
for h in human:
    print(h,human.get(h))

