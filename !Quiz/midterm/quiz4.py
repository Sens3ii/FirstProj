import re
s = input()
move = re.findall('.', s)
ourxy = input().split()
ourx = int(ourxy[0])
oury = int(ourxy[1])
x = int(0)
y = int(0)
result = False
for i in move:
    if ourx == x and oury == y:
        result = True
    elif i == 'R':
        x += 1
    elif i == 'L':
        x -= 1
    elif i == 'U':
        y += 1
    elif i == 'D':
        y -= 1

if result == True:
    print('Passed')
else:
    print('Missed')
