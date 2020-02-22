# Create a function that returns element at index i in input list.
def exercise_1(numbers, index): 
    print(numbers[index])


index = int(input())
numbers = list(map(int,input().split()))
exercise_1(numbers, index)
