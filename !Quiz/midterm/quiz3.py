size = int(input())
numbers = input().split()
if len(numbers) == len(set(numbers)):
    print('YES')
else:
    print('NO')
