n = int(input())  # number of keys
keys = list(map(int, input().split()))  # limit of clicks for every key
k = int(input())  # number of clicks
clicks = list(map(int, input().split()))  # actually clicked keys
countclicks = [0] * n
for key in clicks:
    countclicks[key - 1] += 1
for i in range(n):
    if countclicks[i] > keys[i]:
        print('YES')
    else:
        print('NO')
