phones = []
for i in range(4):
    phones.append(list(input()))
    j = 0
    while j < len(phones[i]):
        if phones[i][j] == '-' or phones[i][j] == '(' or phones[i][j] == ')':
            phones[i].pop(j)
        else:
            j += 1
    if len(phones[i]) == 11:
        phones[i] = phones[i][1:]
    elif len(phones[i]) == 12:
        phones[i] = phones[i][2:]
    elif len(phones[i]) == 7:
        phones[i] = ['4', '9', '5'] + phones[i]
for i in range(1, 4):
    if phones[0] == phones[i]:
        print('YES')
    else:
        print('NO')
