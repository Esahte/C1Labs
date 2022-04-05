x = int(input('enter the lower number: '))
j = int(input('enter the higher number: '))
i = x
print('The even numbers between', x, 'and', j, 'are:', end=' ')
while i <= j:
    if x % 2 == 0:
        print(i, end=' ')
    i += 1

