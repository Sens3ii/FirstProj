a = int(input())
i = -1
j = 1
while j <= a:
    i += 1
    j = 2**i
    if j >= a:
        print(i)
        break
