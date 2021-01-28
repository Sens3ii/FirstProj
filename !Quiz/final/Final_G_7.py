n = int(input())  # input data
matrix = []  # do matrix
newline = []  # init newline for help
for i in range(n):
    line = input().split()  # input data
    for i in line:
        # change values in line list, to integers, and append in newline list
        newline.append(int(i))
    matrix.append(newline)  # append list of integers
    newline = []  # renew newline

for line in sorted(matrix):  # sort matrix
    print(line[0], end=' ')  # printing 1 lines
    print(line[1], end=' ')  # printing 2 lines
    print(line[2])  # not end = ' ' because last line
