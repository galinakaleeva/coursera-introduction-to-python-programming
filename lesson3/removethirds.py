s = input()
l = len(s)
i = l - l % 3
while i >= 0:
    s = s[:i] + s[i+1:]
    i -= 3
print(s)
