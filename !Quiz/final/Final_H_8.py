
# FIRST SOLUTION
# def isPalindrome(data):
#     myDict = dict()
#     withoutPairs = 0
#     for i in data:
#         if i in myDict:
#             myDict[i] += 1
#         else:
#             myDict[i] = 1
#     for i in myDict.values():
#         if i % 2 == 1:
#             withoutPairs += 1
#         if withoutPairs > 1:
#             return "NO"
#     return "YES"

# data = list(input())
# print(isPalindrome(data))


# SECOND SOLUTION
n = int(input())
t = n
reversed_n = 0
while(n > 0):
    one_digit = n % 10
    reversed_n = reversed_n*10+one_digit
    print(reversed_n)
    n = n//10
if(t == reversed_n):
    print("YES")
else:
    print("NO")

# Third solution
# data = input()
# print("YES") if data == data[::-1] else print("NO")
