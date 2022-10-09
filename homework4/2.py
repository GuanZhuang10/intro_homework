l = [1, 2, 3, 4, 5]
index = 4
for i in range(4, -1, -1):
    print(l[i])
while index > -1:
    print(l[index])
    index -= 1
print(l[::-1])