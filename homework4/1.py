result = 1
for i in range(1, 100, 2):
    print(i)
    if i < 50:
        result = result*i
print(result)
