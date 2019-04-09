def sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum(a, b - 1) + 1
    else:
        return sum(a, b + 1) - 1


a = int(input())
b = int(input())
print(sum(a, b))
