inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
words = {}
for line in inFile:
    tempData = line.split()
    for i in range(len(tempData)):
        words[tempData[i]] = words.get(tempData[i], 0) + 1
pairs = []
for word in words:
    pairs.append((words[word], word))
pairs.sort(key=lambda x: (-x[0], x[1]))
for pair in pairs:
    print(pair[1], file=outFile)
inFile.close()
outFile.close()
