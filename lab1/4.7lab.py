import math
n = int(input())
k = int(input())
print(int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))
