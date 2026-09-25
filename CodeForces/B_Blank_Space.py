for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    final = 0
    for i in a:
        if i == 0:
            count += 1
        else:
            count = 0
        if final < count:
            final = count
    print(final)