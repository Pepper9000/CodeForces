for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    a[0] += 1
    ans = 1
    for i in a:
        ans *= i
    print(ans)