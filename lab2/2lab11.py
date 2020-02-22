def Difference(set1, set2):
    print(set1-set2)


numb1 = list(map(int, input().split()))
numb2 = list(map(int, input().split()))
set1 = set(numb1)
set2 = set(numb2)
Difference(set1, set2)
