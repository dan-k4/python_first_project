"""
ループの中でジャンケンを難度もする処理を作成します
相手は必ず、グー、チョキ、パーの順で手を出し、
こちらは入力を受け付けます。
入力すると：あなたの出した手：「」相手の出した手：「」と表示される
相手に勝った場合：あなたは勝ちましたと表示されてループを抜け出せる
負けた場合は：あなたの負け、再チャレンジと表示されて、３回負けるとループを抜け出せ、
「あなたは負けましたと表示され、ループの外に出る
あいこの場合は：あいこと表示される
誤った入力をした場合：再入力をしてくださいと表示される
"""
# def generate_enemy_hand():
#     while True:
#         yield '1'
#         yield '2'
#         yield '3'

# def is_win(my_hand, enemy_hand):
#     if my_hand == '1' and enemy_hand == '2':
#         return True
#     elif my_hand == '2' and enemy_hand == '3':
#         return True
#     elif my_hand == '3' and enemy_hand == '1':
#         return True
#     return False

# hands_dict = {
#     '1':'グー',
#     '2':'チョキ',
#     '3':'パー'
# }

# from random import randint
# lose_count = 0
# enemy_hands = generate_enemy_hand()

# while True:
#     my_hand = input('何を出しますか？１、グー・２、チョキ・３、パー')
#     if my_hand not in ('1','2','3'):
#         print('間違った入力です')
#         continue
#     enemy_hand = str(randint(1,3))
#     print('あなたの出した手は:{},相手の出したては:{}'.format(hands_dict.get(my_hand), hands_dict.get(enemy_hand)))
#     if my_hand == enemy_hand:
#         print('あいこ')
#     elif is_win(my_hand, enemy_hand):
#         print('あなたは勝ちました')
#         break
#     else:
#         lose_count += 1
#         if lose_count == 3:
#             print('あなたは負けました')
#             break
#         else:
#             print('あなたは負けました、再チャレンジ')


def generate_enemy_hand():
    while True:
        yield '1'
        yield '2'
        yield '3'

def is_win(my_hand, enemy_hand):
    if my_hand == '1' and enemy_hand == '2':
        return True
    elif my_hand == '2' and enemy_hand == '3':
        return True
    elif my_hand == '3' and enemy_hand == '1':
        return
    return False

hands_dict = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー'
}
from random import randint
lose_count = 0
enemy_hand = generate_enemy_hand()

while True:
    my_hand = input('1:g,2:t,3:p')
    if my_hand not in ('1','2','3'):
        print('continue')
        continue
        enemy_hand = str(randint(1,3))
    elif my_hand == enemy_hand:
        print('same')
        continue
    elif is_win(my_hand, enemy_hand):
        print('win')
        break
    else:
        lose_count += 1
        if lose_count == 3:
            print('lose')
            break
        else:
            print('again')

