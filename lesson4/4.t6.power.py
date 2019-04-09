def power(a, n):
    pow = 1
    if n >= 0:
        while n > 0:
            pow *= a
            n -= 1
        return pow
    else:
        while n < 0:
            pow /= a
            n += 1
        return pow


a = float(input())
n = int(input())
print(power(a, n))
