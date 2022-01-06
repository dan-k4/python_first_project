# 再帰 => 関数から自分の関数を呼び出すこと
# クラッシュする可能性がある為、使わない方が良い

def sample(a):
    if a < 0:
        return
    else:
        print(a)
        sample(a-1)
sample(10)

# フィボナッチ数列

def fib(n):
    return 1 if n < 3 else fib (n-1) + fib (n-2)

for x in range(1,10):
    print(fib(x))

