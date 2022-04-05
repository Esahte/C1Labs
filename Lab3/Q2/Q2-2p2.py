x = int(input('enter a number: '))
i = 1
print('The integers that are factors of', x, 'are:', end=' ')
while i <= x:
    j = x / i
    if x % i == 0:
        print(i, end=' ')
    i += 1

