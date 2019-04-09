inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
k = int(inputFile.readline())  # number of places
n = 0  # number of people in competition
marks = [0] * 301
for line in inputFile:
    tempLine = list(map(int, line.split()[-3:]))
    if tempLine[0] >= 40 and tempLine[1] >= 40 and tempLine[2] >= 40:
        marks[tempLine[0] + tempLine[1] + tempLine[2]] += 1
        n += 1
sortedMarks = []
i = 300
while i >= 0:
    if marks[i] > 0:
        sortedMarks.append([i, marks[i]])  # i - mark, marks[i] - number
    i -= 1
if sortedMarks[0][1] > k:
    print(1, file=outputFile)
elif n <= k:
    print(0, file=outputFile)
else:
    numberOfEntered = sortedMarks[0][1]
    result = sortedMarks[0][0]
    for pair in sortedMarks[1:]:
        if numberOfEntered + pair[1] <= k:
            numberOfEntered += pair[1]
            result = pair[0]
        else:
            break
    print(result, file=outputFile)
inputFile.close()
outputFile.close()
