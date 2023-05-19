s = input()
j = 0
k = 0
for i in s:
    if (i.isupper()):
        j += 1
    if (i.islower()):
        k += 1
if j > k:
    print (s.upper())
else:
    print (s.lower())