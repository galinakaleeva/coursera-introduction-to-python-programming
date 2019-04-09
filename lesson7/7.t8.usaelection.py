inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
candidates = {}
for line in inFile:
    candidate = line.split()[0]
    votes = int(line.split()[1])
    candidates[candidate] = candidates.get(candidate, 0) + votes
for candidate in sorted(candidates):
    print(candidate, candidates[candidate], file=outFile)
inFile.close()
outFile.close()
