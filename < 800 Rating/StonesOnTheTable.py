n = int(input())
s = input()
j = 0
i = 0
while i < n - 1:
    if s[i] == s[i+1]:
        s = s[:i+1] + s[i+2:]
        j += 1
        n -= 1
    else:
        i += 1
print(j)