# list1 = [1, 2, 3, 4]
# list2 = []
# for i in list1:
#     list2.append(i*2)

# print(list2)


# import math


# def isPrime(x):
#     if x == 1:
#         return False
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True


# list1 = list(range(1, 20))
# list2 = [i for i in list1 if isPrime(i)]
# print(list2)


# list1 = ["Almas", "Jamshut", "Azamat"]
# list2 = [18, 23, 34, 25]
# d = [(list1[i], list2[i]) for i in range(0, len(list1))]
# print(d)
# d2 = zip(list1, list2)
# for i in d2:
#     print(i)

# list1 = [2, 6, 3, 1, 5]
# it = iter(list1)
# #  or it = list1.__iter__
# print(next(it))
# print(next(it))

# list1 = [1, 2, 3, 4, 5]
# it = iter(list1)
# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break


# def generator_example():
#     n = 1
#     print("first")
#     yield n

#     n = 2
#     print("second")
#     yield n


# a = generator_example()
# print(next(a))
# print(next(a))

# def fib():
#     first = 1
#     second = 2
#     while True:
#         yield first, second
#         first, second = second, first + second


# it_fib = fib()
# print(next(it_fib))
# print(next(it_fib))
import math


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# def next_prime():
#     n = 2
#     while True:
#         while not is_prime(n):
#             n = n + 1
#         yield n
#         n = n + 1


# prime = next_prime()
# print(next(prime))
# print(next(prime))
# print(next(prime))
# for i in range(0, 10):
#     print(next(prime))

# list1 = list(range(1, 10))
# print(list1)
# it = (x**2 for x in list1)
# print(next(it))


class Student:
    def __init__(self, name, surname, gpa):
        self.name = name
        self.surname = surname
        self.gpa = gpa

    def calc_gpa(self):
        return self.gpa/2


a = Student(name="AAA", surname="BBB", gpa=3.4)
b = Student(name="fff", surname="ggg", gpa=2.8)
print(a.name, a.surname, a.gpa)
print(b.name, b.surname, b.gpa)
print(a.calc_gpa)
