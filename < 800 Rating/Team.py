f = 0
for i in range(int(input())):
    a,b,c = map(int, input().split())
    x = 0
    if (a == 1):
        x+=1
    if (b == 1):
        x+=1
    if (c == 1):
        x+=1
    if (x >= 2):
        f+=1
print (f)