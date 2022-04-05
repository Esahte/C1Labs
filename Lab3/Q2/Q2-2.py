x = int(input('enter an integer: '))
print('The integers that are factors of', x, 'are:', end=' ')
for m in range(1, x + 1):
    n = 0
    while n <= x:
        j = n * m
        n += 1
        if j == x:
            print(m, end=' ')
    m += 1

