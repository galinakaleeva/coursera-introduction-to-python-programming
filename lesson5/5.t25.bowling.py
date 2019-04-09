NK = list(map(int, input().split()))
N = NK[0]
K = NK[1]
bow = 'I '*N
bow = list(bow.split())
for i in range(K):
    lr = list(map(int, input().split()))
    for j in range(lr[0], lr[1] + 1):
        bow[j - 1] = '.'
bow = ''.join(bow)
print(bow)
