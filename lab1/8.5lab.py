x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r


if IsPointInCircle(x, y, xc, yc, r) == 1:
    print("YES")
else:
    print("NO")
