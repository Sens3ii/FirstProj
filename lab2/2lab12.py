def ExtraSet(numb):
    newSet = set()

    for i in numb:
        temp = i
        while temp in newSet:
            temp *= i
        newSet.add(temp)
    print newSet


numb = list(map(int, input().split()))
ExtraSet(numb)
