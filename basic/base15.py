# 制御分(if文)
# None, False, 0, 空のリスト、"", 辞書、タプル、セット
# 厳密には、__bool__()が定義されているクラスで、Falseが返されるもの
# 変数.__bool__() = bool(変数)

class ClassA():
    
    def __init__(self,a):
        self.a = a
    
    def __bool__(self):
        if self.a == 'a':
            return True
        return False

bool_var = ClassA('a')
print('boolの計算結果:{}'.format(bool(bool_var)))
if bool_var:
    print('if文の中の処理')

