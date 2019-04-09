a = list(map(int, input().split()))
i = 0
while i < len(a):
    n = 1
    j = i + 1
    while j < len(a):
        if a[i] == a[j]:
            a.pop(j)
            n += 1
        else:
            j += 1
    if n > 1:
        a.pop(i)
    else:
        i += 1
print(*a)
