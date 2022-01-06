#セットのメソッド
"""
union(|)ユニオン、和集合を返す
intersection(&)集合の共通する要素、積集合を返します
difference(-)片方の集合にあり、片方の集合にない要素、差集合を返します
symmentric_difference(^)どちらか一方にだけある要素の集合を返します
"""

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

u = s | t #和集合
# u = s.union(t)

print(u)

u = s & t #積集合
# s.intersection(t)

print(u)

u = s - t # 差集合
s.difference(t)

print(u)

u = s ^ t #対象差
#s.symmentric_difference(t)

print(u)

s |= t
print(s)

# issubset, issuperset, isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t)) #別の集合に含まれているか
print(s.issuperset(t)) #別の集合を含んでいるか

print(t.isdisjoint(s)) #重複要素はないか
print(t.isdisjoint(u))