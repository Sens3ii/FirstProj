class Student:
    name = 'Ivan'
    gpa = 4.0
print(Student)
print(dir(Student))
a = getattr(Student,'gpa','Not Found')
print(a)
a1 = getattr(Student,'age','Not Found')
print(a1)
x = hasattr(Student,'gpa')
print(x)
delattr(Student,'gpa')
x1 = hasattr(Student,'gpa')
print(x1)