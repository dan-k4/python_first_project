"""
キャラクターを作成して戦わせる
Characterクラスを作成し、インスタンス変数として
name, hp, offence, defenseを持たせる

attackメソッドを実行すると、敵インスタンスのHPが自分のoffence-敵のdefense分減ります。
（自分のoffense - 敵のdefenseがマイナスの場合は１)

critical_hitメソッドを実行すると, attackメソッドの倍のダメージを与える
HPが０になると死んでしまい、攻撃ができなくなります

AllCharactersクラスを作成します。クラス変数が３個存在します
all_characters:現在作成されているすべてのキャラクター配列
alive_characters:現在生きているすべてのキャラクターの配列
dead_characters:現在死んでいるすべてのキャラクターの配列
もし同じ名前のキャラクターを登録した場合は CharacterAlreadyExistExceptionoを作成して返す
"""
class CharacterAlreadyExistException(Exception):
    pass

class AllCharacters:

    all_characters = []
    alive_characters = []
    dead_characters = []
    
    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターは既に存在しています')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)
    
    @classmethod
    def character_delete(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character:

    def __init__(self, name, hp, offence, defense):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defense = defense

    def attack(self, enemy, critical_point = 1):
        if self.hp <= 0:
            print('キャラクターはすでに死んでいます')
            return
        attack_point = self.offence - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)

    def critical_hit(self, enemy):
        self.attack(enemy, 2)

character_a = Character('A',10, 5, 3)
character_b = Character('B',8, 6, 2)

print(character_b.hp)
character_a.critical_hit(character_b)
print(character_b.hp)
print(AllCharacters.alive_characters)
character_a.attack(character_b)
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
character_b.attack(character_a)

character_c = Character('A',10, 5, 3)

