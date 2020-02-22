def isPalindrome(l):

    newdict = dict()

    for i in l:
        if i in newdict:
            newdict[i] += 1
        else:
            newdict[i] = 1

    withoutPairs = 0
    for i in newdict.values():
        if i % 2 == 1:
            withoutPairs += 1
        if withoutPairs > 1:
            return "No"
    return "Yes"


print(isPalindrome([1, 2, 3, 4, 1]))
print(isPalindrome([1, 2, 3, 1, 2]))
