for _ in range(int(input())):
    p = str(input())
    ans = (int(p[0]) - 1) * 10
    if len(p) == 4:
        ans += 10
    elif len(p) == 3:
        ans += 6
    elif len(p) == 2:
        ans += 3
    elif len(p) == 1:
        ans += 1
    print(ans)