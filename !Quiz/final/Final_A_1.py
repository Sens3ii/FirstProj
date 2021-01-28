h = int(input())  # height
w = int(input())  # width
k = int(input())  # how much

possible = False  # default
for i in range(1, h+1):  # cheking by height
    for j in range(1, w+1):  # cheking by width
        if k == w*i or k == h*j:  # if our byte can be so,
            possible = True  # possible = True
            break  # end internal cycle
    if possible:  # end external cycle
        break

# print depends on possible
print("YES") if possible else print("NO")
