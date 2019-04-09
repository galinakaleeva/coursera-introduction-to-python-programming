def phib(n):  # Fibonacci is spelled with f both in English and Italian
    if n == 1 or n == 2:
        return 1
    return phib(n - 1) + phib(n - 2)


n = int(input())
print(phib(n))
