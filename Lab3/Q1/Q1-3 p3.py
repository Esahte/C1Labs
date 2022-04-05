x = int(input('enter a number: '))
v = int(input('enter decrease: '))

for i in range(x):
    if x <= 0:
        break
    elif x % 2 == 0:
        print(x, 'is even')
    else:
        print(x, 'is odd')
    x -= v
print('Blastoff!!')
