#セット
# 同じ値を持つことができない（ユニーク）
# 順序が保持されていない（挿入された順番通りに取り出すことができない）
# ユニオンやインターセクションなどの集合処理を高速で行うことができる

set_a = {'a','b','c','d','a','12'}
print(set_a)
print('e' in set_a)
print('a' in set_a)
print('a' not in set_a)

print(len(set_a))

#add, remove, discard, pop, clear

set_a.add('A') #要素の追加
print(set_a)
set_a.remove('a') #要素の削除
print(set_a)
set_a.discard(12) #removeとの違いは要素がなかった場合にエラーにならない
print(set_a)
val = set_a.pop()
print(val, set_a)

set_a.clear()
print(set_a)
