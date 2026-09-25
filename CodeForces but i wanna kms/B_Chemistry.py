for i in range(int(input())):
    a, b = map(int, input().split())
    n = list(map(str, input().split()))
    if a % 2 == 0:
        if (len(set(n)) * 2) - len(n) == b:
            print("YES")
        else:
            print("NO")
    else:
        if (len(set(n)) * 2) + 1 - len(n) == b:
            print("YES")
        else:
            print("NO")