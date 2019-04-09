inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
n = int(inputFile.readline())
cup = set()
cap = set()
for i in range(n):
    mi = int(inputFile.readline())
    tempData = []
    for j in range(mi):
        tempData.append(inputFile.readline().strip())
    cup |= set(tempData)
    if i == 0:
        cap = set(tempData)
    else:
        cap &= set(tempData)
print(len(cap), file=outputFile)
for elem in cap:
    print(elem, file=outputFile)
print(len(cup), file=outputFile)
for elem in cup:
    print(elem, file=outputFile)
inputFile.close()
outputFile.close()
