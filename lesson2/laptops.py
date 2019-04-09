s1 = int(input())  # store
s2 = int(input())
s3 = int(input())
b1 = int(input())  # box
b2 = int(input())
b3 = int(input())
n1 = (s1 // b1) * (s2 // b2) * (s3 // b3)
maxnumber = n1
n2 = (s1 // b1) * (s2 // b3) * (s3 // b2)
if n2 > maxnumber:
    maxnumber = n2
n3 = (s1 // b2) * (s2 // b1) * (s3 // b3)
if n3 > maxnumber:
    maxnumber = n3
n4 = (s1 // b2) * (s2 // b3) * (s3 // b1)
if n4 > maxnumber:
    maxnumber = n4
n5 = (s1 // b3) * (s2 // b1) * (s3 // b2)
if n5 > maxnumber:
    maxnumber = n5
n6 = (s1 // b3) * (s2 // b2) * (s3 // b1)
if n6 > maxnumber:
    maxnumber = n6
print(maxnumber)
