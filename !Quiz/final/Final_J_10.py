# FIRST SOLUTION
def isPalindrome(data):
    myDict = dict()
    withoutPairs = 0
    for i in data:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    for i in myDict.values():
        if i % 2 == 1:
            withoutPairs += 1
        if withoutPairs > 1:
            return "JOJO"
    return "ZA WARUDO TOKI WO TOMARE"

data = list(input())
print(isPalindrome(data))


# SECOND SOLUTION
# from collections import Counter
# data = input()
# data_counter = Counter(data)
# possible = 0

# for i in data_counter:
#     if data_counter[i] % 2 == 1:
#         possible += 1

# if len(data) == 1 or possible <= 1:
#     print('ZA WARUDO TOKI WO TOMARE')
# else:
#     print('JOJO')
