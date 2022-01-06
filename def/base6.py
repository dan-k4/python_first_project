"""
ジェネレーター関数は何に使うの？
一番generater使うのは、DBから大量のデータを引っ張る時
DBの大量のレコードを一気に取得して何万行の配列のするとメモリを食う
この場合、generaterを使うと、使用するとメモリをほぼ０にすることができる    
（ただし、generaterの方が処理は遅いので、使うかどうかはケースバイケース
"""

# list, generator memory
import sys
list_a = [i for i in range(100000)]

def num(max):
    i = 0
    while i < max:
        yield i
        i += 1

# for i in num(100000):
#     print(i)

gen = num(100000)
print(sys.getsizeof(gen))
print(sys.getsizeof(list_a))