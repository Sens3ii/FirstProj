# Create a function that deletes elements after given index.
def exercise_5(numbers, index):
    newNumb = []
    for i in range(index):
        newNumb.append(numbers[i])
    print(newNumb)


index = int(input())
numbers = list(map(int, input().split()))
exercise_5(numbers, index)
