#1
num = 10
print(type(num))
num_str = str(num)

num_list = [num_str,'20', '30']
print(num_list)

num_list.append('40')
num_tuple = tuple(num_list)

val = input()
num_tuple += (val,)

num_set = {'40', '50','60'}
print('num_tuple = {}'.format(num_tuple))
print('num_set = {}'.format(num_set))

print(set(num_tuple)|num_set)
num_dict = {num_tuple:num_str}

print(len(num_dict))

print(num_dict.get('Mykey', 'Does not exist'))

num_list.extend(['50','60'])
print('num_list = {}'.format(num_list))

val = input()
is_under_50 =  int(val) < 50
print('is_under_50={}'.format(is_under_50))

print(f'num_str ={num_str}')

print(dir(num_dict))

