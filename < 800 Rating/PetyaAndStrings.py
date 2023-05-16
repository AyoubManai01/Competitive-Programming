a = input()
b = input()
k = 0
for i in range(len(a)):
    if (a[i]==b[i] or a[i].lower()==b[i] or b[i].lower()==a[i]):
        k+=1
    if (ord(a[i].upper())<ord(b[i].upper())):
        print ('-1')
        break;
    if (ord(a[i].upper())>ord(b[i].upper())):
        print ('1')
        break;
if (k == len(a)):
    print ('0')