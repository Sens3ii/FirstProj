# Create a function that reverses a given list.
def exercise_4(numbers):
    numbers.reverse()
    print(numbers)


numbers = list(map(int, input().split()))
exercise_4(numbers)
