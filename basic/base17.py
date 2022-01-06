# all, any 関数
#allはオブジェクトの中が全てTrueの場合に処理をする
#anyはオブジェクトの一部がTureの場合に処理をする

if all((True, True, True, True)):
    print('allの中の処理')

if any((False,False,False,True)):
    print('anyの中の処理')

if not any((False,False,False,True)):
    print('anyの中の処理')