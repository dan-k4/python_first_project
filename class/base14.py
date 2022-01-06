# ファイル書き込み
# ファイルが存在しなければ作成、存在した場合は上書き

#バイナルファイルの読み込み、書き込み mode='rb or wb'
# 上書きモード mode='w'
# 追記モード mode='a'

file_path = 'resources/output.csv'
f = open(file_path, mode='w', encoding='utf-8', newline='\n')
f.write('aaa\nbbb')
f.close()

with open(file_path, mode='a', encoding='utf-8', newline='\n') as f:
    list_a = [
        ['A', 'B', 'C'],
        ['あ','い','う']
    ]
    for x in list_a:
        f.write('\n')
        f.write(','.join(x))
    # f.writelines(list_a[0])

