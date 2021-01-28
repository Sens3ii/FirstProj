size1 = int(input())
students1 = input().split()
size2 = int(input())
students2 = input().split()
missed = []
notingroup = []

check1 = False

for i in students1:
    for j in students2:
        if i == j:
            check1 = True
    if check1 == False:
        missed.append(i)
    check1 = False

check2 = False
for i in students2:
    for j in students1:
        if i == j:
            check2 = True
    if check2 == False:
        notingroup.append(i)
    check2 = False


print("Missed students:")
for i in missed:
    print('- '+i)
print("Not in the group:")
for i in notingroup:
    print('- '+i)
