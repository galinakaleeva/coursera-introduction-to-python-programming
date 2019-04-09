inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
text = []
for line in inputFile:
    text += line.split()
text = set(text)
print(len(text), file=outputFile)
inputFile.close()
outputFile.close()
