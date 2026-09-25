for _ in range(int(input())):
    n, k = map(int, input().split())
    x = 0
    while True:
        m = k // n
        k += m - x
        x = m
        if k // n == m:
            break
    print(k)