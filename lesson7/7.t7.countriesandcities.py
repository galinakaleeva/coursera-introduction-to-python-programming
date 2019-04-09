n = int(input())
myDict = {}
for i in range(n):
    line = input().strip()
    country = line[:line.find(' ')]
    cities = line[line.find(' ') + 1:].split()
    for j in range(len(cities)):
        myDict[cities[j]] = country
m = int(input())
for i in range(m):
    city = input()
    print(myDict[city])
