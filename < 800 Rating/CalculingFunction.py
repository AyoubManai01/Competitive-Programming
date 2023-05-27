n = int(input())
if n % 2 == 0:
    print (n//2)
if n % 2 != 0:
    n = ((n-1)//2)+1
    print ("-"+str(n))