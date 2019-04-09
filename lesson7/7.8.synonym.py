n = int(input())
synonymDict = {}
for i in range(n):
    pair = input().split()
    synonymDict[pair[0]] = pair[1]
    synonymDict[pair[1]] = pair[0]
print(synonymDict[input()])
