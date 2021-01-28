import math
numbers = [10, 12, 19, 21]


def IsEven(n):
    if n % 2 == 0:
        return True
    return False

x = any([IsEven(number) for number in numbers])
print(x)


def IsPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


x1 = any([IsPrime(number) for number in numbers])
print(x1)
