# Create a function that collects only values with even index from a given list
def exercise_2(numbers):
    print(numbers[::2])


numbers = list(map(int, input().split()))
exercise_2(numbers)
