inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
candidates = {}
votes = 0
for line in inFile:
    candidates[line.strip()] = candidates.get(line.strip(), 0) + 1
    votes += 1
pairs = []
for candidate in candidates:
    pairs.append((candidates[candidate], candidate))
pairs.sort(key=lambda x: (-x[0], x[1]))
if pairs[0][0] * 2 > votes:
    print(pairs[0][1], file=outFile)
else:
    print(pairs[0][1], file=outFile)
    print(pairs[1][1], file=outFile)
inFile.close()
outFile.close()
