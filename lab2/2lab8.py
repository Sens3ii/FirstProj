# Create a function that returns both minimum and maximum value of given list.
def MinMax(numbers):
    t = min(numbers), max(numbers)
    print(t)


numbers = list(map(int, input().split()))
MinMax(numbers)
