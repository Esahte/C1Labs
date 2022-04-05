def isPrime(n):
    for j in range(2, n - 1):
        while n > 2:
            if n % j == 0:
                return False
            break
        # j += 1
    return True


i = int(input('enter a number: '))
print(isPrime(i))
