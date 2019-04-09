a = list(map(int, input().split()))
Min = a[0]
indMin = 0
Max = a[0]
indMax = 0
for i in range(len(a)):
    if a[i] < Min:
        Min = a[i]
        indMin = i
    if a[i] > Max:
        Max = a[i]
        indMax = i
a[indMin], a[indMax] = a[indMax], a[indMin]
print(*a)
