# if and or not
#等価性 <, <=, >,>=, !=, ==, not

msg = input('信号の色はblue,red,yellow')
if msg == 'blue':
    print('すすめ')
elif msg == 'red':
    print('止まれ')
else:
    print('それ以外の処理')

age = input('年齢を入力してください')
if age < 20:
    print('20未満')
elif age <= 40: #20以上で実行される
    print('20以上、40以下')
elif age >= 60:
    print('60以上です')
else:
    print('それ以外の年齢')

# and or not
gender = 'man'
age = 10
if gender == 'man' and age <20:
    print('未成年男性です')

gender = 'man'
age = 10
if gender == 'man' or age <20:
    print('男性もしくは20歳未満です')

if not gender == 'man':
    print('男性ではありません')