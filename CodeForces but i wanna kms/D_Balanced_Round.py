for _ in range(int(input())):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        y = []
        for i in x:
            