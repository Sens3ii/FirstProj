def f(x):
    if x < 18:
        return False
    else:
        return True
print(f(20))
ages = [5,11,17,18,32,24]
adults = filter(f,ages)
l = list(adults)
print(l)
