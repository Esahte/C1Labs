x = int(input('enter a number: '))

while 1 <= x:
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, 'is odd')
    x -= 1
print('Blastoff!!')
