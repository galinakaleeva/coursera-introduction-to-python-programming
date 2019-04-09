def CountSort(a):
    c = [0] * 101
    for number in a:
        c[number] += 1
    k = 0
    for i in range(101):
        for j in range(c[i]):
            a[k] = i
            k += 1
    return(a)


a = list(map(int, input().split()))
print(*(CountSort(a)))
