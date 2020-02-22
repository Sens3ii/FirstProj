def SuperSet(s):
    s2 = set()
    for i in s:
        s2.add(i-1)
        s2.add(i+1)
    print(s2)


numbers = list(map(int, input().split()))
s = set(numbers)
SuperSet(s)
