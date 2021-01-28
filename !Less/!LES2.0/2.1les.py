my_tuple = (1,2,3) # we can't change tuple cuz its immutable,strings too
print(my_tuple)
t = (1,"Hello",3.4)
print(t)
t2 = ("Hello",[8,4,6],[1,2,3])
t2[1][1] = "X" # we can change list in tuple
print(t2)
print(my_tuple[0:2])
print(my_tuple+t)
print(my_tuple*3)

