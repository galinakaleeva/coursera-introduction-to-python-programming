inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
partFromSchools = [0] * 100
for line in inputFile:
    tempData = line.split()
    partFromSchools[int(tempData[2])] += 1
maxNumber = 0
result = []
for i in range(100):
    if partFromSchools[i] > maxNumber:
        maxNumber = partFromSchools[i]
        result = [i]
    elif partFromSchools[i] == maxNumber:
        result.append(i)
print(*result, file=outputFile)
inputFile.close()
outputFile.close()
