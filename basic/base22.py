#例外処理(try, except)
# 例外処理：実行時に発生するエラー（実行エラー）を制御して処理を行う
# try:
#     処理
# except エラー名:
#     例外発生時の処理

# FileNotFoundError:プログラムで指定されたファイルが見つからないエラー
# IndexError:配列などで指定したインデックスに値が存在しないエラー
# TypeError:方に関するエラー
# ZeroDivisionError:0で割ろうとしたことによるエラー
# ExceptionError:全ての例外

try:
    a =10 /0
    b = [10,20,30]
    a =b[4]
    c = b.method_a()
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()
    # print(e, type(e))
    pass
except IndexError as e:
    print('indexerror発生')
except Exception as e:
    print('ExceptionError', e, type(e))
else:
    # a = 10 / 0
    print('Else')
finally:
    print('finally')


print('処理が完了しました。')

# else:例外が発生しなかった場合に実行され、例外が発生した場合には実行されない
# finally例外が発生した場合にも、発生しなかった場合にも実行される


