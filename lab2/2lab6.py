# Create a function that inserts elements at given index and then deletes elements after given index.
def exercise_6(numbers, index1, index2, newelement):
    newNumb = []
    numbers.insert(index1, newelement)
    for i in range(index2):
        newNumb.append(numbers[i])
    print(newNumb)


print("List: ")
numbers = list(map(int, input().split()))
index1 = int(input("Insert index: "))
index2 = int(input("Deleting index: "))
newelement = int(input("Inserted element: "))
exercise_6(numbers, index1, index2, newelement)
