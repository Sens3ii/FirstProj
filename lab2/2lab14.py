def NewLists(numb, index):
    s = set()
    for i in numb:
        if i > index:
            s.add(i)
    print(s)


index = int(input())
numb = list(map(int, input().split()))
NewLists(numb, index)
