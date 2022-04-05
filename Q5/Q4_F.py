def isPrime(n):
    for j in range(1, n - 1):
        j += 1
        while n > 2:
            if n % j == 0:
                return False
            break
    return True
