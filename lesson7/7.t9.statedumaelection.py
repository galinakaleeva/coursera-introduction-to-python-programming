inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
parties = []
votes = 0
i = 0
for line in inFile:
    tempData = line.strip()
    name = line[:line.rfind(' ')]
    number = int(line[line.rfind(' ') + 1:])
    parties.append([number, i, name])
    votes += number
    i += 1
numOfPart = i
places = [0] * numOfPart
quot = []
for i in range(numOfPart):
    quot.append([i, 0, parties[i][1]])
firstQuot = votes / 450
vacantPlaces = 450
for i in range(numOfPart):
    places[i] = parties[i][0] // firstQuot
    quot[i][1] = parties[i][0] % firstQuot
    vacantPlaces -= places[i]
quot.sort(key=lambda x: (-x[1], -x[2], x[0]))
i = 0
while vacantPlaces != 0:
    places[quot[i][2]] += 1
    vacantPlaces -= 1
    i += 1
    i %= numOfPart
for i in range(numOfPart):
    print(parties[i][2], int(places[i]), file=outFile)
inFile.close()
outFile.close()
