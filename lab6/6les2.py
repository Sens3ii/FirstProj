x = any([True,False,True]) # if one of them is True or 1
print(x)
numbers = [1,10,100,1000,10000]
l = [number for number in numbers if number > 10]
print(l)
x1 = any([number < 10 for number in numbers])
print(x1)
