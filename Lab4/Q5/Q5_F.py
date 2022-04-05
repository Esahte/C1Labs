from Q4_F import isPrime


def trickWithPrime(n1, n2):
    for i in range(n1, n2 + 1):
        if isPrime(i):
            r = (pow(i, 2) + 17) % 12
            print(r, i)
        # i += 1


# They all have the same remainder


trickWithPrime(4, 40)
