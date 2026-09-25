for _ in range(int(input())):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    if x == sorted(x):
        print("YES")
    elif k == 1 and len(set(x)) > 1:
        print("NO")
    else:
        print("YES")