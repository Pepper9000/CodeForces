for _ in range(int(input())):
    a = input()
    ans = a[0]
    if len(a) == 2:
        print(a)
    else:
        for i in a[1:-1:2]:
            ans += i
        print(ans + a[-1])