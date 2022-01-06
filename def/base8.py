# 高階関数
# 関数を引数にしたり、返り値にする関数を高階関数という

def print_hello():
    print('hello')

def print_goodby():
    print('goodbye')

var = ['A','B',print_hello, print_goodby]
var[2]()
var[3]()

def print_world(msg):
    print('{} world'.format(msg))

def print_konnnichiwa():
    print('こんにちわ')

def print_hello(func):
    func('hello')
    return print_konnnichiwa

var = print_hello(print_world)
var()