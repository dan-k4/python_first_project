#変数の応用

animal = 'dog'
print(animal)

# 定数

LEGAL_AGE = 20
age = 18
if age < LEGAL_AGE: #ageが20よりも小さい時に処理を実行
    print('未成年')
else:
    print('成人')


#特殊なformat文
print(f'age = {age}') # 3.6
print(f'{age=}') #3.8
