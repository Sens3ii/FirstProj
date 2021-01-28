s = input().split()
bigWord = ''
for i in s:
    if len(i) > len(bigWord):
        bigWord = i
print(str(bigWord) + '\n' + str(len(bigWord)))
