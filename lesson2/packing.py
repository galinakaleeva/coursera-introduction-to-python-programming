l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
if l1 > w1:
    l1, w1 = w1, l1
if l2 > w2:
    l2, w2 = w2, l2
if lc > wc:
    lc, wc = wc, lc
if w1 > w2:
    l1, l2 = l2, l1
    w1, w2 = w2, w1
if h1 + h2 <= hc:
    if l1 <= lc and l2 <= lc and w2 <= wc:
        print('YES')
    else:
        print('NO')
elif h1 <= hc and h2 <= hc:
    par1 = w2 <= wc and l1 + l2 <= lc
    par2 = w2 <= lc and l1 + l2 <= wc
    orth1 = w2 <= wc and l2 + w1 <= lc
    orth2 = w2 <= lc and l2 + w1 <= wc
    orth3 = w2 + l1 <= wc and w1 <= lc and l2 <= lc
    orth4 = w2 + l1 <= lc and w1 <= wc and l2 <= wc
    if par1 or par2 or orth1 or orth2 or orth3 or orth4:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
