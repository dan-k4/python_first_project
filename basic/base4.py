# 数値について
# int型
# float型
value = 1

print(value)
value = -2
print(value)
value = value + 4 # 2
print(value * 4)
print(value / 3)
value = 10
print (value // 3)
print(value % 3)

value += 3
value -+ 2
print(value)
print(value ** 3)

#浮動小数点数
height = 175.5
print(height)
print(type(height))
print(height + 10) #10がint型に自動的に変換される



# +:足し算 -:引き算 *:掛け算 /:割り算 //:割り算(小数点以下切り下げ） %:剰余 **:べき乗
# <<, >> シフト演算
value = 8 # 1000 => 0010
print(value >> 2)
print(value << 3) # 1000 => 1000000

# 論理積、論理和（＆、｜）

print(12 & 21) #01100 and 10101 = 00100 => 4
print(12|21) # 01100 or 10101 = 11101 => 29

value = 12
value &= 21 #value = value & 21
print(value)