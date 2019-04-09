n = int(input())
peopleList = []
for i in range(n):
    peopleList.append(input().split())
peopleList.sort(key=lambda x: -int(x[1]))
for i in range(n):
    print(peopleList[i][0])
