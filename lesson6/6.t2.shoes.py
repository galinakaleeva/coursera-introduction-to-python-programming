size = int(input())
s = list(map(int, input().split()))
s.sort()
found = 0
pairs = 0
for i in s:
    if i >= size and found == 0:
        found = 1
        current = i
        pairs += 1
    if found == 1 and i - current >= 3:
        current = i
        pairs += 1
print(pairs)
