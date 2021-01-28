list = [1, 2, 3, 4, 5, 5, 6, 7, 8]
print(list[2:5])
print(list[2:-2])
list[1:4] = [10, 11, 12]
print(list)
list.append("Hello world")
print(list)
list.extend(['a', 'b'])
print(list)
print([1, 2, 3] * 3)
list.insert(1,"abc")
print(list)
del list[1]
print(list)
list.remove("Hello world") #by element
print(list)
