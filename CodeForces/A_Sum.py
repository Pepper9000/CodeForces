for i in range(int(input())):
    a = list(map(int, input().split()))
    print("YES" if sum(a) == max(a) * 2 else "NO")