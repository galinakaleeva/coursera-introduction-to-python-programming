numOfTowns = int(input())
tempTown = list(map(int, input().split()))
numOfShelters = int(input())
tempShelter = list(map(int, input().split()))
town = []
shelter = []
for i in range(numOfTowns):
    town.append((tempTown[i], i + 1))
for i in range(numOfShelters):
    shelter.append((tempShelter[i], i + 1))
town.sort()
shelter.sort()
mapping = []
j = 0
index = 0
for i in range(numOfTowns):
    minDist = abs(town[i][0] - shelter[index][0])
    for j in range(index, numOfShelters):
        tempDist = abs(town[i][0] - shelter[j][0])
        if tempDist < minDist:
            minDist = tempDist
            index = j
        if tempDist > minDist:
            break
    mapping.append((town[i][1], shelter[index][1]))
mapping.sort()
for i in range(numOfTowns):
    print(mapping[i][1], end=' ')
