#タプルとリストの違い、値を変更、追加できない
#配列よりもタプルの方が、アクセスするスピードが速い
#ハッシュ化して辞書型のキーとして利用できる
#値を変更したくないような値を用いる場合に、値が変更されないことを保証できる

#タプル

fruit = ('apple', 'banana', 'lemon')
print(fruit)
print(type(fruit))
print(fruit[0])

# fruit[1] = 'grape'
fruit = fruit + ('grape',)
print(fruit)

list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit)
print(fruit.count('apple'))
print(fruit.index('apple'))

pos = 135, 35
countries = {pos: 'japan'}
print(countries.get((135,35)))

