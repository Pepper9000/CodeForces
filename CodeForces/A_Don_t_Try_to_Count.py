for _ in range(int(input())):
    n, m = map(int, input().split())
    x, s = input(), input()
    count = 0
    for i in range(6):
        if s not in x:
            x += x
            count += 1
        else:
            break
    if s not in x:
        print(-1)
    else:
        print(count)