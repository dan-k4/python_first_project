# ファイル入力

# read, readlinesはファイルをすべて一気に読み込むため、処理は速いがメモリの消費は大きい（小さいファイル向け）
# readlineはファイルを一行ずつ読み込むため、処理は遅いがメモリの消費は小さい。（大きいファイル向け）

# *with、ファイルのopen,closeを自動的に行う*

# セイウチ演算子

file_path = 'resources/input.csv'
f = open(file_path, mode='r', encoding='utf-8')

# line= f.read() # 中身全体
# print(line)

# lines = f.readlines()
# print(lines)
# for x in lines:
#     print(x.rstrip('\n'))

line = f.readline()
while (line := f.readline()):
    print(line.rstrip('\n'))
    # line = f.readline()

f.close() #ファイルを閉じる
# →メモリをくう、他の処理でファイルに開けなくなってくる

# with
with open(file_path, mode='r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)

# print(f.read()) -> ファイルを閉じているので実行できない
