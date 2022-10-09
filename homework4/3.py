ans = 0
l = input()
flag = 0
for i in range(len(l)):
    max1 = 1
    j = i+1
    while j<len(l) and l[i] == l[j] :
        j += 1
        max1 += 1
    ans = max(max1,ans)
    i = j - 1
print(ans)
