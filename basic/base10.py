#辞書：ディクショナリー
# 辞書型の宣言：{}
# 取り出し：dict['key']
# dict.get('key','')

car = {'brand': 'Toyota', 'model':'Prius','year':2015}
print(car['brand']) #対応する値がなかった場合：error
print(car.get('brand')) #対応する値がなかった場合：none
print(car.get('bran', 12)) #第一引数がなかった場合、第二引数を返す

print(car.get(1))

# キーの一覧：keys()
# 値の一覧：values()
# キーと値の一覧:items()

print(car.keys())
print(car.values())
print(car.items())

for k, v in car.items():
    print('key = {}, value = {}'.format(k,v))

if 'brand' in car:
    print('CARのブランドは{}'.format(car['brand']))

