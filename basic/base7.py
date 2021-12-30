#文字列型
#文字列型の宣言’’、””
#複数行にまたがる宣言”””〜”””

fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)

fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + 'banana'
print(new_fruit)

fruits = """
apple
banana
grape
"""

print(fruits)

fruit = 'banana'
print(fruit[2])
print(fruits[-1])

# encode, decode => bytes[]

byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

# count

msg = 'abcdefgabcd'
print(msg.count('abc'))

# startswith, endswith

print(msg.startswith('abc'))
print(msg.endswith('d'))

#文字列の除去　strip, rstrip（右端, lstrip（左端,

msg = ' abc '
print(msg)
print(msg.strip())
print(msg.rstrip())

msg = 'abcdefabc'
print(print(msg.strip('cba')))
print(print(msg.rstrip('cba')))
print(print(msg.lstrip('cba')))

#大文字変換：upper, 小文字変換：lower, 大文字・小文字入れ替え：swapcase, 文字変換：replace, 最初だけ大文字に変換：capitalize

msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u, msg_l, msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF', 1)
print(msg_r)

msg = 'hello WoRld'
print(msg.capitalize())

#文字列の一部取り出し、format, isloewr, isupper

msg = 'hello, my name is taro'
print(msg[:7])
print(msg[6:])
print(msg[1:6])
print(msg[1:10:2])

print('hello{}'.format('Taro'))
name = 'Jiro'
print(f'hello{name}')
print(f'{name=}')

msg = 'apple'
print(msg.islower())
print(msg.isupper())

#fint, index, rfind, rindex
# find, rfind:文字列のインデックスを検索
# 見つからない場合は-1
# index, rindex:文字列のインデックスを検索
# 見つからない場合はエラー

msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))

# エラーの場合の挙動が違う
print(msg.find('ABCE'))
print(msg.index('ABCE'))

