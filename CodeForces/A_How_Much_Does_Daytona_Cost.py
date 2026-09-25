for _ in range(int(input())):
    x, y = map(int, input().split())
    n = list(map(int, input().split()))
    if y in n:
        print("YES")
    else:
        print("NO")