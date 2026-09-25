for _ in range(int(input())):
    n = int(input())
    a = set(map(int, input().split()))
    if len(a) - 1 == max(a) - min(a) or len(a) == 1:
        print("YES")
    else:
        print("NO")