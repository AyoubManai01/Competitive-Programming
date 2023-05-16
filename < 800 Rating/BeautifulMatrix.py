j = 2
for i in range(5):
    a,b,c,d,e = map(int, input().split())
    if (i==4):
        j=2
    if (a==1 or e==1):
        f =j+2
    if (b==1 or d==1):
        f = j+1
    if (c==1):
        f = j
    if (j==0):
        j=2
    j-=1
print (f)