n, k = map(int, input().split())
strikes = set()
for i in range(k):
    a, b = map(int, input().split())
    strikes |= set(range(a, n+1, b))
holidays = set(range(6, n + 1, 7)) | set(range(7, n + 1, 7))
strikes -= holidays
print(len(set(strikes)))
