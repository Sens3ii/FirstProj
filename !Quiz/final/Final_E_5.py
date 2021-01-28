import re  # regex


def check(data):
    # search by pattern in data, to take span()
    possible = re.search("[a-z]+@[a-z]+\.[a-z]+", data)
    # if span()[0] - initial index of searching == 0 - it means that our key on the right position, + check ends position
    if possible and possible.span()[0] == 0 and possible.span()[1] == len(data):
        print("Yes")
    else:
        print("No")


data = input()  # input data
check(data)
