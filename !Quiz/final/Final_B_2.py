names_set = set()  # set of students names
students = dict()  # dictionary for cheking

n = int(input())  # max data count

for i in range(n):  # do checking n times
    name, date = input().split()  # input in one line
    names_set.add(name)  # adding name in names
    if name not in students:  # if new name, its value becomes set
        students[name] = set()
    students[name].add(date)  # adding value to key
    # print(students[name])  # for me, to see


names_set = sorted(names_set)  # sorting set
for name in names_set:
    print(name, end=" ")  # print name
    if len(students[name]) >= 3:
        print("+1")  # if student have more/equal dates, +1
    else:
        print("NO BONUS")  # elif print No
