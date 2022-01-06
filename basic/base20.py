# continue : ループ内にcontinueがあると、処理が一度飛ばされます。
# break:breakが実行されるとループの外に処理が出ます。
# else:ループの外に出た際に実行される(breakでループを抜けた場合には実行されません）

for i in range (10):
    if i == 3:
        continue
    print(i)


for i in range (10):
    if i == 3:
        break
    print(i)


for i in range (10):
    if i == 3:
        continue
    print(i)
else:print('ループ処理終了')

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    if num == 7:
        break
    print(num)
    num += 1

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print('whileループ終了')

