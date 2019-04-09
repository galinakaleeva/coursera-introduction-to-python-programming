inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
words = {}
for line in inFile:
    tempData = line.split()
    for i in range(len(tempData)):
        words[tempData[i]] = words.get(tempData[i], 0) + 1
maxFreq = 0
for word in words:
    if words[word] > maxFreq:
        outputWord = word
        maxFreq = words[word]
    elif words[word] == maxFreq and word < outputWord:
        outputWord = word
print(outputWord, file=outFile)
inFile.close()
outFile.close()
