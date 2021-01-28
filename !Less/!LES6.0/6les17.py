def f(a,b):
    return a + b
print(f(1,2))
x = map(f,(1,2,3),(4,5,6))
for t in x:
    print(t)