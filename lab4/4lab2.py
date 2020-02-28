import json
ourList = {}
for i in range(int(input('Range:'))):
    name = input()

    score = input()

    ourList[name] = score
y = json.dumps(ourList)

with open('4lab2text.txt', mode='w') as file:
    file.write(y)
