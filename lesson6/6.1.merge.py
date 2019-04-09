def merge(a, b):
    i = 0
    j = 0
    la = len(a)
    lb = len(b)
    ab = []
    while i < la or j < lb:
        if i < la and j < lb and a[i] < b[j]:
            ab.append(a[i])
            i += 1
        elif i < la and j < lb:
            ab.append(b[j])
            j += 1
        elif i < la:
            ab.append(a[i])
            i += 1
        else:
            ab.append(b[j])
            j += 1
    return ab


a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = merge(a, b)
print(*ab)
