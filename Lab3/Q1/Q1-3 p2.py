x = int(input('enter a number: '))
j = int(input('enter decrease: '))

while 1 <= x:
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, 'is odd')
    x -= j
print('Blastoff!!')
