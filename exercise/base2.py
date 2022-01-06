for i in range(100):
    print(i)

for i in range(100):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('Fizz and Buzz')
    else:
        print(i)

#answer
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('{}:FizzBuzz'.format(i))
    elif i % 3 == 0:
        print('{}:Fizz'.format(i))
    elif i % 5 == 0:
        print('Buzz:{}'.format(i))
    else:
        print(i)
