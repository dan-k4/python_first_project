# リスト内包表記
# ループと条件を使って、一行でリストを作成する方法
# 変数名 = [式 for 変数 in リスト(if 条件式)]
"""
value = [x for x in range (100000)] リスト
tup = tuple (x for x in range(1000000)) タプル
gen = (x for x in range(100000)) ジェネレータ
set = {x for x in range(1000000)} セット
"""

list_a = (1,2,3,4,'a','b') #tuple
list_b = [x * 2 for x in list_a if type(x) == int] #list_a => list_b
print(list_b)

list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)

dict_a = {
    'a':'Apple',
    'b':'Banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x) == str]
print(list_c)

list_a = (x for x in range(100))
print(type(list_a))

def func(n):
    for x in range(2, n):
        if n % x == 0:
            return True
        return False

list_a = [x for x in range(100) if func(x) == False]
print(list_a)

