"""
リスト変数を使うと１つの箱の中に複数の値を入れることができる
（Java)などの言語と違って、最初にリストのサイズを指定しなくても良い
"""
#リスト
list_a = [1,2,3,4]
list_b = []

print(list_a)
print(list_a[2])
print(list_a[-2])

list_a = [1, [1,2,'apple'],3,'banana']
print(list_a[1][2])
print(list_a)
list_a[1][2] = 'lemon'
print(list_a)

#リストのメソッド
#リストのスライス
list_a = [1,2,3,4,5]
list_b = list_a[:3]
list_c = list_a[1:4:2]
print(list_b)
print(list_c)

#append, extend, insert, clear

list_a.append('apple')
print(list_a)
list_a.extend(['banana', 'melon'])
print(list_a)
list_a.insert(1, 'grape')
print(list_a)
list_a.clear()
print(list_a)

#remove, pop, count, index
list_a = [0,1,1,2,2,3,3,4]
list_a.remove(3)
print(list_a)
value = list_a.pop()
print(list_a, value)
print(list_a.count(1))
print(list_a.index(1))

#copy, リストの中身のコピーを返す
print(list_a)
list_b = list_a.copy()
list_b[0] = 'AAAA'
print(list_a)

#sort, 要素の昇順並び替え
# reverse,要素の逆順並び替え

list_a = ['banana', 'apple','lemon','grape']
print(list_a)
list_a.sort()
list_a = sorted(list_a)
list_a.reverse()
print(list_a)