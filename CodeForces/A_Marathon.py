for _ in range(int(input())):
    a = list(map(int, input().split()))
    count = 0
    for i in a[1:]:
        if i > a[0]:
            count += 1
    print(count)