from Q4_F import isPrime


def primes(n1, n2):
    for i in range(n1, n2 + 1):
        if isPrime(i):
            print(i, end=' ')


print(primes(2, 10))
