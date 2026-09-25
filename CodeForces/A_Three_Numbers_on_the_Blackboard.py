for _ in range(int(input())):
    a = list(map(int, input().split()))
    possible = True
    while possible == True:
        a = sorted(a)
        if a[0] + a[1] < a[2]:
            a[2] = a[0] + a[1]
        else:
            possible = False
    print(a[2] - a[0])