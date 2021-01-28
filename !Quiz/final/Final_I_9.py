data = input().split()  # input

n = int(data[0])  # first integer = n
m = int(data[1])  # second integer = m
for i in range(n, m + 1):  # cheking integers between n and m
    if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:  # if if if
        print(i, end=' ')  # print in one line
