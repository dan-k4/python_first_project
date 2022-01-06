# メタクラス
# メタクラスとはクラスの再定義をするクラス
# デフォルトのメタクラスはtypeクラスだが、自身で定義することもできる
# 主に、クラスの定義をその定義で良いのか検証する際に用いられる

class MetaException(Exception):
    pass

class Meta1(type): #type(デフォルトのメタクラス)

    def __new__(metacls, name, bases, class_dict):
        print('metacls ={}'.format(metacls))
        print('name = {}'.format(name))
        print('bases = {}'.format(bases))
        print('class_dict = {}'.format(class_dict))
        # if 'my_var' not in class_dict.keys():
        #     raise MetaException('my_varを定義してください')
        for base in bases: #継承しているクラス
            if isinstance(base, Meta1):
                raise MetaException('継承できません') #finalクラス
        return super().__new__(metacls, name, bases, class_dict)

class ClassA(metaclass = Meta1):
    a = '123'
    my_var = '246'
    pass

class SubClassA(ClassA):
    pass

