#論理型とは、TrueとFalseの二つの値を扱う変数の型
is_animal = True
if is_animal:
    print('動物です')

is_man = True
is_adult = False

# or文
if is_man or is_adult:
    print('男か大人です')

# and文
if is_man and is_adult:
    print('成人男性です')