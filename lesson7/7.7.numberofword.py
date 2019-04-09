inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
myDict = {}
for line in inFile:
    words = line.split()
    for i in range(len(words)):
        myDict[words[i]] = myDict.get(words[i], -1) + 1
        print(myDict[words[i]], end=' ', file=outFile)
inFile.close()
outFile.close()
