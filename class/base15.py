# withの詳細
"""
with クラス as a:
    処理

withの処理を実行する前に、
withの後に指定したクラスの、__init__,__enter__がそれぞれ呼ばれ、
処理終了時に、クラスの__exit__メソッドが呼ばれる

どのように使うか？
処理が連続している処理が連続していてすべての処理が必要な場合。
（例）
ファイルの書き込み処理（ファイルを開く→書き込む→ファイルを閉じる
DBへのデータの書き込み処理（DBコネクションを貼る→書き込む→コネクションを閉じる
"""

class WithTest:
    
    def __init__(self, file_name):
        print('init called')
        self.__file_name = file_name
    
    def __enter__(self):
        print('enter called')
        self.__file = open(self.__file_name, mode='w', encoding='utf-8')
        return self
    
    def write(self, msg):
        self.__file.write(msg)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit called')
        self.__file.close()

with WithTest('resources/output.txt') as t:
    print('inside with')
    t.write('aaa')
