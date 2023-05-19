n = int(input())
s = input()
j = 0
k = 0
for i in s:
    if (i == 'A'):
        j += 1
    if (i == 'D'):
        k += 1
if j > k:
    print ('Anton')
if j < k:
    print ('Danik')
if j == k:
    print ('Friendship')