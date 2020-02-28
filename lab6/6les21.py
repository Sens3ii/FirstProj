test = [1,2,3,4,5,6,7,2,2,3,4,4,4,4,4]
x = set(test)
print(x)
print(test.count(4))
a = max(set(test),key = test.count)
print(a)