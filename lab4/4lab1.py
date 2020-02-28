import json
with open("4lab1text.txt", mode='r') as file:
    f = file.read()
ourDict = json.loads(f)

print(ourDict)
#convert from file in python by джейсон стэтхэм
