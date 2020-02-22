import math
s = str(input())
c = int(len(s))
b = float(c/2)
a = int(math.ceil(b))
print(s[a:]+s[0:a])
