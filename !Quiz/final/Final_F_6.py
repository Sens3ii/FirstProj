n = int(input())
stolbi = [int(i) for i in input().split()]
ranges = int(input())


def devil(n, stolbi, ranges):
    for lr in range(ranges):
        l, r = [int(i) for i in input().split()]
        count = current_height = 0
        for i in range(l, r + 1):
            if stolbi[i] > current_height:
                current_height = stolbi[i]
                count += 1
        print(count)


devil(n, stolbi, ranges)
