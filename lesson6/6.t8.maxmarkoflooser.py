inputFile = open('input.txt', 'r', encoding='utf8')
outputFile = open('output.txt', 'w', encoding='utf8')
max9, secMax9, max10, secMax10, max11, secMax11 = 0, 0, 0, 0, 0, 0
for line in inputFile:
    tempData = line.split()
    form = int(tempData[2])
    mark = int(tempData[3])
    if form == 9:
        if mark > max9:
            max9, secMax9 = mark, max9
        elif max9 > mark > secMax9:
            secMax9 = mark
    if form == 10:
        if mark > max10:
            max10, secMax10 = mark, max10
        elif max10 > mark > secMax10:
            secMax10 = mark
    if form == 11:
        if mark > max11:
            max11, secMax11 = mark, max11
        elif max11 > mark > secMax11:
            secMax11 = mark
print(secMax9, secMax10, secMax11, file=outputFile)
inputFile.close()
outputFile.close()
