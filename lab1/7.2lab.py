a = int(input())
i = 2
while i <= a:
    if a % 2 == 0:
        print(2)
        break
    elif a % i == 0:
        print(i)
        break
    i += 1
