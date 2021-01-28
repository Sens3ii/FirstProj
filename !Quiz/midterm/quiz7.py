import re
txt = input()
t = input()
s = input()
f = input()
newtxt = txt.replace(t, s)
result = re.findall(f, newtxt)
print(len(result))
