# Create a function that mutates elements to square after given index. Elements before given index do not chang
def exercise_3(numbers, index):
    newNumb = []
    for i in range(len(numbers)):
        if i <= index:
            newNumb.append(numbers[i])
        else:
            newNumb.append(numbers[i]*numbers[i])
    print(newNumb)


index = int(input())
numbers = list(map(int, input().split()))
exercise_3(numbers, index)
