import math
a = int(input())
x1 = int(a * 45);
x2 = int(math.ceil((a-1)/2))
x3 = int(math.floor((a-1)/2))
x2 = int(x2*5)
x3 = int(x3*15)
res = int(x1+x2+x3)
hours = int(res//60)
minutes = int(res%60)
print(9+hours,minutes)