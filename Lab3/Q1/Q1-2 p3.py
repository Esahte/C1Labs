x = int(input('enter a number: '))

for i in range(x):
    if x % 2 == 0:
        print(x, 'is even')
    else:
        print(x, 'is odd')
    x -= 1
print('Blastoff!!')
