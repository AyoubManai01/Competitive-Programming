for i in range(int(input())):
    ch = input()
    if(len(ch)>10):
        print(ch[0]+str((len(ch)-2))+ch[-1])
    else:
        print(ch)