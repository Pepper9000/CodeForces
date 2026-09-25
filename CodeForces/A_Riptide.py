for _ in range(int(input())):
    a = sorted(list(map(int, input().split())))
    count = 0
    while len(set(a)) > 2:
        a[0] += 1
        a[2] -= 1
        count += 1
    print(count)