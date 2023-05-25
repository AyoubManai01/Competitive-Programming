s = input()
a = []
for i in s:
    if i not in {'+'}:
        a.append(i)
b = sorted(a)
c = ""
for i in b:
    c += i
    c += '+'
c = c[:-1]
print (c)