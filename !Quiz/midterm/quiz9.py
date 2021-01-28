size = int(input())
numbers = input().split()
index = int(input())
numbers = numbers[0:size]
halfOne = numbers[0:index]
halfTwo = numbers[index:size+1]
firstNumber = int("".join(halfOne))
secondNumber = int("".join(halfTwo))
result = firstNumber*secondNumber
print(result)
