def isperfectSquare(n):
    t = 0
    while t < n:
        t += 1
        m = pow(t, 2)
        if m == n:
            return True
    return False
