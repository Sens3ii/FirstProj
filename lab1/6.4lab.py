import math
s = str(input())
c = int(len(s))
b = int(s.find(" "))
print(s[b+1:]+" "+s[0:b])