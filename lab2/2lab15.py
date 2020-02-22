def exercise_15(numb):
    ans = 0
    for i in numb[1::2]:
        if i % 2 == 1:
            ans += 1
    print(ans)


numb = list(map(int, input().split()))
exercise_15(numb)
# 0,3,11,2,44,23,4