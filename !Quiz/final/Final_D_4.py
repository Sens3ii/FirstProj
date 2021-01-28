data = input().split()  # input

l = int(data[0])  # left limit
r = int(data[1])  # right limit

if l % 2 == 0:  # if left limit we do odd, for logic of function
    l += 1


def odd_rec(l, r):  # function of odd number by recursion
    if l > r:  # if limit, close function
        return
    print(l, end=' ')  # print every time l
    odd_rec(l + 2, r)  # return function again - rectursion


odd_rec(l, r)  # do function
