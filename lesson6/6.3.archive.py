array0 = list(map(int, input().split()))
N = array0.pop()  # number of users
space = array0.pop()  # space on disc
array = []
for i in range(N):
    array.append(int(input()))
array.sort()
data = 0
i = 0
while data <= space and i < N:
    data += array[i]
    i += 1
if data > space:
    print(i - 1)
else:
    print(i)
